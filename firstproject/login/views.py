from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect


# Create your views here.

def welcome(request):
    return render(request, 'login/welcome.html')