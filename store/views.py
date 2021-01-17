from django.shortcuts import redirect, Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView, DetailView
from django.views import View
from store.models import Store
from products.models import Product


# Create your views here.
class StoreList(ListView):
    model = Product
    paginate_by = 3
    context_object_name = 'products'
    # template_name = 'products/product_list.html'

    def get_queryset(self):
        qs = super().get_queryset()

        # get store slug
        slug = self.kwargs.get('slug', None)

        # filter store products
        qs = qs.filter(store__slug__iexact=slug)
        return qs


class StoreDetails(DetailView):
    model = Store
    context_object_name = 'store'
    slug_url_kwarg = 'slug'
    # query_pk_and_slug = re

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #
    #     # get store slug
    #     slug = self.kwargs.get('slug', None)
    #
    #     # filter store products
    #     qs = qs.filter(store__slug__iexact=slug)
    #     return qs
