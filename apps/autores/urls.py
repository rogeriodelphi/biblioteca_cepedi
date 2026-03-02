from django.urls import path
from apps.autores import views


app_name = 'apps.autores'

urlpatterns = [
    path('inserir_autor/', views.inserir_autor, name='inserir_autor'),
]
