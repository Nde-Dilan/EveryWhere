from django.contrib import admin

# Register your models here.

from django.contrib import admin


# Register your models here.
from .models import *

@admin.register(Proprietaire)
class Proprio(admin.ModelAdmin):
    pass


@admin.register(Client)
class Client(admin.ModelAdmin):
    pass


@admin.register(HSE)
class HSE(admin.ModelAdmin):
    pass


@admin.register(Maison)
class Maison(admin.ModelAdmin):
    pass


@admin.register(Studio)
class Studio(admin.ModelAdmin):
    pass


@admin.register(Salle)
class Salle(admin.ModelAdmin):
    pass


@admin.register(Terrain)
class Terrain(admin.ModelAdmin):
    pass


@admin.register(PlanImmobilier)
class PlanImmobilier(admin.ModelAdmin):
    pass
@admin.register(TypeHSE)
class TypeHSE(admin.ModelAdmin):
    pass