from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blink, name='blink'),
    path('dashboard/', views.dash, name='dashboard'),
    path('login/', views.loginusr, name='loginusr'),
    path('logout/', views.logoutusr, name='logoutusr'),
    path('register/', views.register, name='register'),
    path('dummyup/', views.fileup, name='dummyup'),
    path('patients/', views.patienttab, name='patientstab'),
    path('addpatient/', views.addpatient, name='addpatient'),
    path('patients-detail/<int:patid>', views.patientsdet, name='patientsdet'),
    path('patients/s/', views.search_patient, name='searchpat'),
]
