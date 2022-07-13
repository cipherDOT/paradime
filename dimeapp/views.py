from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Question, Answer
from .forms import AnswerForm, QuestionForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def index(request):

    # queriws all the objects that are questions
    questions = Question.objects.all()

    # The question form
    form = QuestionForm()

    # If the page sends a POST request...
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        # if it is a valid form...
        if form.is_valid():

            # save the form with the instance user
            form.instance.user = request.user
            form.save()

        return redirect('index')

    # context dictionary
    context = { 
        'request'   : request,
        'questions' : questions,
        'form'      : form
    }
    
    return render(request, 'dimeapp/index.html', context)

# the question view page
@login_required(login_url='login')
def view(request, key):

    # queries all the objects that are questions
    question = Question.objects.get(id=key)

    # queriws all the objects that are answers linked
    # to the question in concern
    answers = Answer.objects.filter(question=question)

    form = AnswerForm()

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.question = question
            form.save()

        return redirect('view', question.id)

    context = {
        'request' : request,
        'question': question,
        'answers' : answers,
    }

    return render(request, 'dimeapp/view.html', context)

@login_required(login_url='login')
def update_question(request, key):
    question = Question.objects.get(id=key)

    form = QuestionForm(instance=question)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()

        return redirect('index')

    context = {
        'request'  : request,
        'form'     : form,
        'question' : question,
    }

    return render(request, 'dimeapp/updateques.html', context)

@login_required(login_url='login')
def update_answer(request, key):
    answer = Answer.objects.get(id=key)
    question = answer.question
    form = AnswerForm(instance=answer)

    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()

        return redirect('view', question.id)

    context = {
        'request': request,
        'form'   : form,
        'answer' : answer,
    }

    return render(request, 'dimeapp/updateans.html', context)

# delete a specific question
@login_required(login_url='login')
def delete_question(request, key):
    question = Question.objects.get(id=key)
    answers = Answer.objects.filter(question=question)

    # if the person who is attempting to delete 
    # it is the person who made it...
    if request.user == question.user:

        # delete all the related answers
        for answer in answers:
            answer.delete()

        # finally delete the question
        question.delete()
    else:
        return redirect('index')

    return redirect('index')


# delete a specific answer
@login_required(login_url='login')
def delete_answer(request, key):

    # get the answer with a specific id
    answer = Answer.objects.get(id=key)

    # queery the related question for redirection
    question = answer.question

    # if the request user is the creation user...
    if request.user == answer.user:
        answer.delete()

    # else redirect them to the main page...
    else:
        return redirect('index')
        
    # if deleted, redirect them to the question page
    return redirect('view', question.id)

def register(request):
    # if an user if registered/authenticated then redirect them to the home page
    if request.user.is_authenticated:
        return redirect('index')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'dimeapp/register.html', context)


def loginuser(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # checks whether the username and password are correct,
        # and is present in the user-database
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # it logins the user
            return redirect('index')

        else:
            messages.info(request, 'Username OR Password is incorrect!!!')
    context = {}
    return render(request, 'dimeapp/login.html', context)

@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('login')