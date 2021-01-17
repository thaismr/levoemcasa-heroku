from django.urls import path, include
from . import views
from products.views import ProductDetails

# Create a namespace for these urls
# store:<path_name>
app_name = 'store'

urlpatterns = [
    # path('', views.StoreList.as_view(), name='list'),
    path('<str:slug>', views.StoreDetails.as_view(), name='list'),
    path('<str:store>/<str:slug>', ProductDetails.as_view(), name='details'),
    # path('category/<str:slug>', views.CategoryChildren.as_view(), name='children'),
    # path('category/<str:parent>/<str:slug>', views.CategoryDetails.as_view(), name='details'),
]
