from django.shortcuts import get_list_or_404, get_object_or_404, render
#from django.http import HttpResponse
#from utils.recipes.factory import make_recipe
from .models import Category, Recipes

def home(request):
    recipes = Recipes.objects.filter(is_published = True,).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes':recipes,
        })

def recipe(request, id):  # Essa função buscA O ID da recipes
    recipe = get_object_or_404(Recipes, 
        pk= id,
        is_published = True,
        )
        
    return render(request, 'recipes/pages/recipe_views.html', context={
        'recipe':recipe,
        'is_details_page':True
        })

def categoria(request, category_id):
    recipes = get_list_or_404(Recipes.objects.filter(
        category__id= category_id,
        is_published = True,
        ).order_by('-id')
        )

    return render(request, 'recipes/pages/category.html', context={
        'recipes':recipes,
        'title': f'{recipes[0].category.name } - categoria |', # Filtra o campo do titulo da categoria por nome
        })

