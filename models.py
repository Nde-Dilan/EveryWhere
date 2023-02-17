"""Lorsque j'essai de faire que les classes Studio,Maison ... heritent de la classe HSE je me retrouve avec une erreur pourtant je trouve pas d'erreurs dans mon code """
from django.db import models


# Create your models here.

class Proprietaire(models.Model):
    Nom_et_prenom = models.CharField(max_length=100)
    Numero_telephone = models.IntegerField()
    e_mail = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return self.Nom_et_prenom

    class Meta:
        verbose_name = "Allocateurs(propriétaire d'HSE)"


class Client(models.Model):
    Nom_et_prenom = models.CharField(max_length=100)
    Numero_telephone = models.IntegerField()
    e_mail = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return self.Nom_et_prenom


class HSE(models.Model):
    author = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    Lieu = models.CharField(max_length=200)
    Prix = models.IntegerField(default=0)
    Date_published = models.DateField(null=True)
    is_already_occupied = models.BooleanField(default=False)
    Surface_totale = models.IntegerField(default=0)

    def louer(self):
        if not self.is_already_occupied :
            return  "🥲 Sorry the location is already occupied. You can look for other HSE 👌"
        return "🚀 Thanks for choosing this , you will get in touch with the owner soon !!"


class Maison(models.Model):
    Nombre_appartements = models.IntegerField(default=1)
    Duree_location = models.TextField()

    # description = models.TextField()


class Terrain(models.Model):
    Nombre_appartements = models.IntegerField(default=1)


class Salle(models.Model):
    Nombre_appartements = models.IntegerField(default=1)
    caracteristiques = models.TextField()
    Duree_location = models.TextField()


class Studio(models.Model):
    Nombre_appartements = models.IntegerField(default=1)
    description = models.TextField()
    Duree_location = models.TextField()


