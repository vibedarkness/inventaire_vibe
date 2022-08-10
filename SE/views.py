from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from SE.EmailBackend import EmailBackend



# Create your views here.
def login_page(request):
    return render(request, 'adminSE/login.html')

def do_login(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackend.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("dingo")

        else:
            messages.error(request,"Email ou mot de passe invalide")
            return HttpResponseRedirect("/")


def index(request):
    return render(request, 'adminSE/index.html')

