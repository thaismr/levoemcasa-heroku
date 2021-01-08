from django.urls import path
from . import views

# Create a namespace for these urls
# categories:<path_name>
app_name = 'categories'

urlpatterns = [
    path('', views.ListCategories.as_view(), name='list'),
]
