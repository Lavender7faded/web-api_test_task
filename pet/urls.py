from django.urls import path, re_path

from . import views

urlpatterns = [
    path('add/', views.pet_form, name='pet_add'),
    path('pet_edit/<int:pk>/', views.pet_form, name='pet_edit'),
    path('pet_delete/<int:pk>/', views.pet_delete, name='pet_delete'),
    path('', views.type_search, name='search'),
]