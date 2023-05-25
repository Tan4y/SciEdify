from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.app, name='app'),
    path('app/biology.html', views.biology, name = 'biology'),
    path('app/chemistry.html', views.chemistry, name='chemisty'),
    path('app/geography.html', views.chemistry, name='geography'),
    path('app/mathematics.html', views.chemistry, name='mathematics')
]