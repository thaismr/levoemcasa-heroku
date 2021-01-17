from django.shortcuts import redirect, Http404
from django.shortcuts import render
from django.db.models import Q, Count, Case, When
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from django.views import View
from store.models import Store
from . models import Category


# Create your views here.
class CategoryList(ListView):
    model = Category
    paginate_by = 4
    context_object_name = 'categories'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(parent=None)
        qs = qs.annotate(
            count_stores=Count('store'),
            count_children=Count('children'),
        )
        return qs


class CategoryChildren(ListView):
    model = Category
    paginate_by = 4
    template_name = 'categories/category_children.html'
    context_object_name = 'categories'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('parent')     # Optimized query to get parent data

        # get slug for this category
        slug = self.kwargs.get('slug', None)

        if not slug:
            return qs

        # filter children with this parent's slug
        qs = qs.filter(parent__slug__iexact=slug)
        qs = qs.annotate(
            count_stores=Count('store'),
        )
        return qs


class CategoryDetails(ListView):
    model = Store
    paginate_by = 3
    context_object_name = 'stores'
    template_name = 'categories/category_details.html'

    def get_queryset(self):
        qs = super().get_queryset()

        # get slug for this category
        slug = self.kwargs.get('slug', None)

        # filter stores in this category
        qs = qs.filter(categories__slug__icontains=slug)
        return qs
