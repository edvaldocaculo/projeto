from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='recipe-home'),
    path('recipes/<int:id>/', views.recipe, name='recipe-details'),
    path('recipes/category/<int:category_id>/', views.categoria, name='category'),
]