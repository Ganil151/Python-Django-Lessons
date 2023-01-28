# pylint: disable=missing-function-docstring
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from . models import Feature

# Create your views here.

# HTML Views


def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

# Register Views


def register(request):
    if request.method != 'POST':
        return render(request, 'register.html')
    password = request.POST['password']
    password2 = request.POST['password2']

        # Error Checking Conditions
    if password == password2:
        username = request.POST['username']
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Used')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username Already Used')
            return redirect('register')
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            return redirect('login')
    else:
        messages.info(request, 'Password Not The Same')

# Login Views


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authentication
        user = auth.authenticate(username=username, password=password)

        # Error Checking Conditions
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
    return render(request, 'login.html')

# Logout Views


def logout(request):
    auth.logout(request)
    return redirect('/')

# Counter Views


def counter(request):
    text = request.GET['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount/': amount_of_words})


# Lesson Stopped at: , from: https://youtu.be/jBzwzrDvZ18?t=22129
