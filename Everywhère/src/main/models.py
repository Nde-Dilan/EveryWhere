from django.db import models, migrations
from django.contrib.auth.models import User


# Create your models here.


class Proprietaire(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE, null=True)
    tel = models.IntegerField()

    def __str__(self):
        return str(self.user)

    class Meta:

        verbose_name = "Allocateurs(propriétaire d'HSE)"


class Client(models.Model):
    # id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE, null=True)
    tel = models.IntegerField()

    def __str__(self):
        return str(self.user)


class HSE(models.Model):
    author = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    Lieu = models.CharField(max_length=200)
    Prix = models.IntegerField(default=0)
    Date_published = models.DateField(null=True, auto_now_add=True)
    is_already_occupied = models.BooleanField(default=False)
    Surface_totale = models.IntegerField(default=0)


class HSEreserve(models.Model):
    ClientId = models.ForeignKey(Client, on_delete=models.CASCADE)
    HSEmain = models.ForeignKey(HSE, on_delete=models.CASCADE)
    Date_reserved = models.DateField(auto_now_add=True)
    # btn = models.B


class Maison(models.Model):
    hse = models.OneToOneField(HSE, blank=True, on_delete=models.CASCADE, null=True)

    Nombre_appartements = models.IntegerField(default=1)
    Duree_location = models.TextField()

    # description = models.TextField()


class Terrain(models.Model):
    hse = models.OneToOneField(HSE, blank=True, on_delete=models.CASCADE, null=True)
    Nombre_appartements = models.IntegerField(default=1)


class Salle(models.Model):
    hse = models.OneToOneField(HSE, blank=True, on_delete=models.CASCADE, null=True)
    Nombre_appartements = models.IntegerField(default=1)
    caracteristiques = models.TextField()
    Duree_location = models.TextField()


class Studio(models.Model):
    hse = models.OneToOneField(HSE, blank=True, on_delete=models.CASCADE, null=True)
    Nombre_appartements = models.IntegerField(default=1)
    description = models.TextField()
    Duree_location = models.TextField()
