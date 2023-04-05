from django.shortcuts import render
from .models import *


# Create your views here.
# def index(request):
#     template = "main/index.html"
#     context = dict()
#     return render(request, template, context)



def index(request):
	template = "main/index.html"
	all_description = PlanImmobilier.objects.all()

	return render(request,template,{"list": all_description})


