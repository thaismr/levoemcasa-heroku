from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from . models import Category


# Create your views here.
class ListCategories(ListView):
    model = Category
    context_object_name = 'categories'
    paginate_by = 3
