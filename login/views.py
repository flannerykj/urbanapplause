from django.contrib.auth import login, authenticate
from .forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import HttpResponse
import json

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password, email=email)
            login(request, user)
            return redirect('profile:main')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
