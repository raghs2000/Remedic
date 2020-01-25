from django.shortcuts import render
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addNewDisease, name='add'),
    path('view', views.viewDiseases, name='view'),
    path('delete/<str:diseaseName>/', views.deleteDisease, name='delete'),
    path('disease/<str:diseaseName>', views.scan2, name='disease'),
]
