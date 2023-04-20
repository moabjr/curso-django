# from django.http import HttpResponse
from django.shortcuts import render


# Criando as view do Projeto Recipes.
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Moab Lima',
    })


# Criando as view do Projeto Recipes.
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Moab Lima',
    })
