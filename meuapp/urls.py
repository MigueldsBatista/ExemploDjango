from django.urls import path, include
from . import views

app_name = 'meuapp'

urlpatterns = [
    path('exemplo/', views.SightView.as_view(), name="novoapp"),
]
