from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.Registro.as_view(), name='registro'),
]
