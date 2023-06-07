from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('math/', views.math, name = 'math'),
    path('app/', views.app, name='app'),
    path('app/biology.html', views.biology, name = 'biology'),
    path('app/chemistry.html', views.chemistry, name='chemisty'),
    path('app/geography.html', views.geography, name='geography'),
    path('app/mathematics.html', views.mathematics, name='mathematics')
]