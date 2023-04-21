# from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Criando as view do Projeto Recipes.


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


# Criando as view do Projeto Recipes.
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
    })
