from django.urls import path
from . import views

urlpatterns = [
        path('', views.sortear , name="sortear"),
        path('agregarPremio/', views.agregar_premio , name="agregarPremio"),
        path('quitarPremio/<int:id>', views.quitar_premio , name="quitarPremio"),
]