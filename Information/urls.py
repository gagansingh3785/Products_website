from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_page, name='login'),
    path('register', views.register_page, name='register'),
    path('information', views.user_information, name='information'),
    path('logout', views.user_logout, name='logout'),
    path('homeB', views.homeB, name='homeB'),
    path('homeS', views.homeS, name='homeS'),
    path('profileB', views.profileB, name='profileB'),
    path('update', views.update, name='update'),
    path('cancel/<int:pk>', views.cancel_order, name='cancel'),
    path('shop/<str:category>', views.shop, name='shop'),
    path('confirm/<int:pk>', views.place_order, name='confirm'),
    path('success/<int:pk>', views.order_success, name='success'),
    path('add', views.add_product, name='add'),
    path('edit/<int:pk>', views.edit_product, name='edit'),
    path('remove/<int:pk>', views.remove, name='remove'),
    path('profileS', views.profileS, name='profileS'),
    path('Cart', views.cart, name='Cart'),
    path('add_cart/<int:pk>', views.add_cart, name='add_cart'),
    path('remove_cart/<int:pk>', views.remove_cart, name='remove_cart'),

]

