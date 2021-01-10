from django.urls import path
from . import views

# Create a namespace for these urls
# categories:<path_name>
app_name = 'categories'

urlpatterns = [
    path('', views.CategoryList.as_view(), name='list'),
    path('category', views.CategoryList.as_view(), name='list'),
    path('category/<str:slug>', views.CategoryChildren.as_view(), name='children'),
    path('category/<str:parent>/<str:slug>', views.CategoryDetails.as_view(), name='details'),
]
