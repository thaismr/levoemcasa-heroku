from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from . models import Category


# Create your views here.
class ListCategories(ListView):
    model = Category
    paginate_by = 3
    context_object_name = 'categories'

    def get_queryset(self):
        qs = super().get_queryset()
        # qs = qs.select_related('parent')     # Optimized query to get related category data
        qs = qs.filter(parent=None)
        return qs
