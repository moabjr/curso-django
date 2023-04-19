# from django.http import HttpResponse
from django.shortcuts import render


# Criando as view do Projeto Recipes.
def home(request):
    return render(request, 'recipes/pages/home.html')
