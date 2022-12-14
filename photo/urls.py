from django.urls import path
from . import views 

urlpatterns = [
    path('', views.gallery, name="gallary"),
    path('photo/<str:pk>/', views.viewPhoto, name="photo"),
    path('add/', views.addPhoto, name="add"),
    path('category/', views.addCategory, name="category")
    
]