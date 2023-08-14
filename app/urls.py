from django.urls import path
from app.views import home, contato, sobre 

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
]