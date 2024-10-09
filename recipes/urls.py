from django.urls import path

from recipes.views import home, contato, sobre

urlpatterns = [
    path('', home, name='home'),  # Home
    path('sobre/', sobre, name='sobre'),  # Sobre
    path('contato/', contato, name='contato'),  # Contato
]
