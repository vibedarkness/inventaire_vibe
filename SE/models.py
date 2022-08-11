
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    user_type_data=((1,"ADMIN"), (2,"STAFF"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=20)

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Staffs(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()



class Client(models.Model):
    prenom= models.CharField( max_length=255)
    nom= models.CharField( max_length=255)
    adresse= models.CharField(max_length=255)
    telephone= models.CharField(max_length=255)
    type_de_client_choices = [
        ('PERSONNE', 'personne'),
        ('ENTREPRISE', 'Entreprise'),
    ]
    type_de_client = models.CharField(
        max_length=10,
        choices=type_de_client_choices,
        default='PERSONNE',
    )
    domaine_activite= models.CharField(max_length=255)

class Fournisseur(models.Model):
    nom=models.CharField(max_length=255)
    adresse= models.CharField(max_length=255)
    telephone=models.CharField(max_length=255)


class Produit(models.Model):
    nom=models.CharField(max_length=255)
    date_achat= models.DateField()
    description=models.TextField()
    date_expiration=models.DateField()
    fournisseur_id=models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    quantite= models.IntegerField(max_length=100)
    prix= models.IntegerField(max_length=255)


class Commande(models.Model):
    client_id=models.ForeignKey(Client, on_delete=models.CASCADE)
    produit_id=models.ForeignKey(Produit, on_delete=models.CASCADE)
    date_commande=models.DateTimeField()
    status_choices = [
        ('LIVRER', 'livrer'),
        ('NON LIVRER', 'non livrer'),
    ]

    status= models.CharField(max_length=10, choices=status_choices, default='LIVRER')
    quantite_commande= models.IntegerField(max_length=100, null=False, default=0)





