from msilib.schema import Class
from django.contrib import admin
from .models import Category, Recipes

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipes) #outra forma de registrar a aplicação na área administrativa
class RecipesAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)