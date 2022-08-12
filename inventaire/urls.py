"""inventaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inventaire import settings
from django.conf.urls.static import static
from SE import views

urlpatterns = [
    path('', views.login_page, name="show_login"),
    path('do_login', views.do_login, name="do_login"),
    path('index', views.index, name="index"),
    path('nouveau_client', views.nouveau_client, name="nouveau_client"),
    path('nouvelle_commande', views.nouvelle_commande, name="nouvelle_commande"),
    path('nouveau_fournisseur', views.nouveau_fournisseur, name="nouveau_fournisseur"),
    path('nouveau_produit', views.nouveau_produit, name="nouveau_produit"),
    path('liste_fournisseur', views.liste_fournisseur, name="liste_fournisseur"),
    path('liste_produit', views.liste_produit, name="liste_produit"),
    path('liste_vente', views.liste_vente, name="liste_vente"),
    path('do_client', views.do_client, name="do_client"),
    path('do_fournisseur', views.do_fournisseur, name="do_fournisseur"),
    path('liste_client', views.liste_client, name="liste_client"),
    path('do_produit', views.do_produit, name="do_produit"),
    path('__debug__/', include('debug_toolbar.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
