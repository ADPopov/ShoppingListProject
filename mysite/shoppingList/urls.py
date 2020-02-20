from django.urls import path

from . import views

app_name = 'shoppingList'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/vote/', views.vote, name='vote'),

    path('add/', views.add, name='add'),
]