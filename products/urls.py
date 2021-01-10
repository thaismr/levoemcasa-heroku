from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='post_index'),
    path('', views.ProductIndex.as_view(), name='index'),
    # path('post/<int:pk>', views.PostDetails.as_view(), name='post_details'),
    # path('category/<str:category>', views.PostCategory.as_view(), name='post_category'),
    # path('search/', views.PostSearch.as_view(), name='post_search'),
]
