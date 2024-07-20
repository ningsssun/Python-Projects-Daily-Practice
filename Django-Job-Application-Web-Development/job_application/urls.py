from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # the home page should be connected to view.index
    path('about/', views.about, name='about')
]