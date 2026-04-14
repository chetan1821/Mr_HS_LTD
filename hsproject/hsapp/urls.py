from django.urls import path
from hsapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("about/",about,name="about"),
    path('market/', market, name="market"),
    path('services_ac/',services_ac,name="services_ac"),
    path('investment/',investment,name="investment"),
    path('sip-calculator/', sip_calculator, name='sip_calculator'),
    
]
