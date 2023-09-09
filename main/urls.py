from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('product/detail/<int:id>', views.product_detail, name="product_detail"),
  path('shopping-cart', views.add_to_cart, name="add_to_cart"),
  path('buy-product', views.buy_now, name="buy_now"),
  path('profile', views.profile, name="profile"),
  path('address', views.address, name="address"),
  path('orders', views.orders, name="orders"),
  path('checkout', views.checkout, name="checkout"),
  path('category/mobile', views.mobile_category, name="mobile_category"),
  path('registration', views.registration, name="registration"),
  path('login', views.login, name="login"),
]
