from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'core/home.html')


@login_required
def pagina1(request):
    return render(request, 'core/pagina1.html')


@login_required
def pagina2(request):
    return render(request, 'core/pagina2.html')