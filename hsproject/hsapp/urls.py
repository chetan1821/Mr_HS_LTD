from django.urls import path
from hsapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("about/",about,name="about"),
    path('market/', market, name="market"),
    
]
