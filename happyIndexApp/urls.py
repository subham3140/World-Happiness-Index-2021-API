from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('v1/country', views.searchByCountry, name="searchByCountry"),
    path('v1/score-range', views.searchByLadder, name="searchByLadder"),
]