from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mission/', views.mission, name='mission'),
    path('board/', views.board, name='board'),
    path('history/', views.history, name='history'),
    path('events/', views.events, name='events'),
    path('join/', views.join, name='join'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('scholarships/', views.scholarships, name='scholarships'),
    path('affiliates/', views.affiliates, name='orgs'),
    path('contact/', views.contact, name='contact'),
]

