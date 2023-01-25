
import email
from http.client import HTTPResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from login.views import *
from login.urls import *



def homepage(request):
    return render(request,"index.html")

def products(request):
    return render(request,"products.html")

def thanks(request):
    return render(request,"thankyou.html") 

def prod_des(request):
    return render(request,"mycainegel.html")


def contact(request):
    try:
        if request.method == "POST":           
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['Message']

            url = "/thn?output={}".format("sent")
            return redirect(url)
    except:

        pass
    return render(request,"contact.html") 

def annual_return(request):
    return render(request,"annual_return.html")