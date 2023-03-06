from django.urls import path, include
from manageForms.views import *

urlpatterns = [
    path('signup/', indexsignup, name='form-signup'),
    path('signin/', indexsignin, name='form-login'),
    path('forgotpassword/', indexforgotpass, name='form-forgotpassword'),
]
