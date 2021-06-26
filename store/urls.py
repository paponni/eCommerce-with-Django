from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns =[
    path('',views.store,name="store"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('updateItem/',views.updateItem,name="updateItem"),
    path('processOrder/',views.processOrder,name="processOrder"),
    path('viewProduct/<int:id>',views.viewProduct,name="viewProduct"),
    path('login/',auth_views.LoginView.as_view(template_name='store/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='store/logout.html'),name='logout'),
    path('register/',views.register,name='register'),
    path('search/',views.search,name='search'),

]