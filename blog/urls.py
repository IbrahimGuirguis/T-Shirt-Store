from django.urls import path
from . import views

urlpatterns = [
    path('buyt-shirts', views.buy_tshirt, name = 'buyt-shirts'),
    path('men', views.men, name = 'men'),
    path('women', views.women, name = 'women'),
    path('shoppingcart', views.shopping_cart, name = 'shoppingcart'),
    path('<int:post_id>', views.product_details, name = 'product_details'),
]