from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm, AnswerForm
from .models import User, Question

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('quiz_start', user_id=user.id)
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def quiz_start(request, user_id):
     return render(request, 'quiz_start.html', {'user_id': user_id})



def quiz_question(request, user_id, question_id):
    question = Question.objects.get(id=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            # Get the selected option from the form
            selected_option = form.cleaned_data['selected_option']

            # Create and save the user's answer
            answer = Answer.objects.create(user=user, question=question, selected_option=selected_option)

            # Determine the next question ID 
            next_question_id = question.id + 1

            # Redirect to the next question or a completion page if there are no more questions
            next_question = Question.objects.filter(id=next_question_id).first()
            if next_question:
                return redirect('quiz_question', user_id=user_id, question_id=next_question.id)
            else:
                # Redirect to a completion page 
                return redirect('quiz_completed')
    else:
        form = AnswerForm()
        form.fields['option'].choices = [
            (1, question.option1),
            (2, question.option2),
            (3, question.option3),
            (4, question.option4),
        ]
    return render(request, 'quiz_question.html', {'form': form, 'question': question})














