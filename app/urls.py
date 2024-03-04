from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mission/', views.mission, name='mission'),
    path('activism/', views.activism, name='activism'),
    path('cultural/', views.cultural, name='cultural'),
    path('join/', views.join, name='join'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('events/', views.events, name='events'),
    path('scholarships/', views.scholarships, name='scholarships'),
    path('orgs/', views.orgs, name='orgs'),
    path('contact/', views.contact, name='contact')
]