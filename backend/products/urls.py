from django.urls import path

from .views import product_details_view, product_list_create_view, product_alt_view

urlpatterns = [
    path('', product_alt_view,),

    path('<int:pk>/', product_alt_view, name='product-details')
 ]