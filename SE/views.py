from ast import Return
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from SE.EmailBackend import EmailBackend
from SE.models import Client, Fournisseur, Produit



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

def nouveau_client(request):
    return render(request, 'adminSE/nouveau_client.html')

def nouvelle_commande(request):
    return render(request, 'adminSE/nouvelle_commande.html')

def nouveau_fournisseur(request):
    return render(request, 'adminSE/nouveau_fournisseur.html')



def liste_client(request):
    clients=Client.objects.all()
    return render(request, 'adminSE/liste_client.html',{"clients":clients})

def liste_fournisseur(request):
    fournisseur=Fournisseur.objects.all()
    return render(request, 'adminSE/liste_fournisseur.html',{"fournisseur":fournisseur})

def liste_produit(request):
    return render(request, 'adminSE/liste_produit.html')

def liste_vente(request):
    return render(request, 'adminSE/liste_vente.html')


def do_client(request):
    if request.method!="POST":
            return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        nom=request.POST.get("nom")
        telephone=request.POST.get("telephone")
        adresse=request.POST.get("adresse")
        domaine_activite=request.POST.get("domaine")
        type_de_client=request.POST.get("type_de_client")
        

        try:
            client=Client(nom=nom,telephone=telephone,adresse=adresse,domaine_activite=domaine_activite,type_de_client=type_de_client)
            client.save()
            messages.success(request,"Ajout avec Success")
            return HttpResponseRedirect(reverse("liste_client"))
        except:
            messages.error(request,"Echec de l'ajout")
            return HttpResponseRedirect(reverse("nouveau_client"))

def do_fournisseur(request):
    if request.method!="POST":
            return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        nom=request.POST.get("nom")
        telephone=request.POST.get("telephone")
        adresse=request.POST.get("adresse")
        

        try:
            fournisseur=Fournisseur(nom=nom,telephone=telephone,adresse=adresse)
            fournisseur.save()
            messages.success(request,"Ajout avec Success")
            return HttpResponseRedirect(reverse("liste_fournisseur"))
        except:
            messages.error(request,"Echec de l'ajout")
            return HttpResponseRedirect(reverse("nouveau_fournisseur"))


def do_produit(request):

    if request.method!="POST":
            return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        nom=request.POST.get("nom")
        date_achat=request.POST.get("date_achat")
        description=request.POST.get("description")
        date_expiration=request.POST.get("date_expiration")
        quantite=request.POST.get("quantite")
        prix=request.POST.get("prix")
        fournisseur_id=request.POST.get("fournisseur")
        fournisseur=Fournisseur.objects.get(id=fournisseur_id)
        

        try:
            produit=Produit(nom=nom,date_achat=date_achat,description=description,date_expiration=date_expiration,quantite=quantite,prix=prix,fournisseur_id=fournisseur)
            produit.save()
            messages.success(request,"Ajout avec Success")
            return HttpResponseRedirect(reverse("liste_produit"))
        except:
            messages.error(request,"Echec de l'ajout")
            return HttpResponseRedirect(reverse("nouveau_produit"))

def nouveau_produit(request):
    produit=Produit.objects.all()
    fournisseur=Fournisseur.objects.all()
    return render(request, 'adminSE/nouveau_produit.html',{"produit":produit,"fournisseur":fournisseur})