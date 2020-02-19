from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/edit/', views.edit, name='Редактирование'),
    path('add/', views.add, name='Редактирование'),
]