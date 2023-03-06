from django.http import HttpResponse
from django.shortcuts import render

from manageForms.forms import *

""" Vue pour s'enregistrer sur le site"""


def indexsignup(request):
    print(request.method)
    template = "manageForms/signup.html"
    if request.method == "POST":
        form = SingUpForm(request.POST)
        print(f"--------------------------{form}-----------------------")
        if form.is_valid():
            form_data_clean = form.cleaned_data
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            form.save()  # utilisateur enregistré dans la table auth_user
            """Ici j'ai essayé de rediriger le user vers la page d'acceuil avec redirect mais j'ai pas réussit à le 
                       faire"""
            return HttpResponse("Inscription réussie!!")
    else:
        form = SingUpForm()

    return render(request, template,
                  context={"form": form})


""" Vue pour se connecter sur le site"""


def indexsignin(request):
    template = "manageForms/login.html"
    return render(request, template)


"""Mot de passe oublié"""


def indexforgotpass(request):
    return render(request, 'manageForms/forgot-password.html', {})
