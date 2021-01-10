from django.shortcuts import redirect, Http404
from django.db.models import Q, Count, Case, When
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib import messages
# from comments.forms import CommentForm
# from comments.models import Comment
from .models import Product


# Create your views here.
class ProductIndex(ListView):
    model = Product
    paginate_by = 3
    context_object_name = 'listings'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('categories')     # Optimized query to get related categories data
        qs = qs.order_by('-id').filter(is_published=True)
        # qs = qs.annotate(
        #     count_comments=Count(
        #         Case(
        #             When(comment__comment_is_published=True, then=1)
        #         )
        #     )
        # )
        return qs
