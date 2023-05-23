from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.app, name='app'),
    path('app/chemistry.html', views.chemistry, name='chemisty'),
]