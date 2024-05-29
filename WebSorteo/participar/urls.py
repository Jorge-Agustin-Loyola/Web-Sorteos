from django.urls import path
from . import views

urlpatterns = [
    path('', views.participar, name="participar"),
    path('verdetalle/<int:id>', views.verDetalle , name="VerDetalle"),
    
]