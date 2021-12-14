from django.urls import path
from . import views

app_name='ecommerce'

urlpatterns=[
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('',views.Home.as_view(),name='home'),
    path('home/',views.Home.as_view(),name='home'),
    path('products/',views.ProductsView.as_view(),name='products'),
    path('addproduct/',views.AddProductView.as_view(),name='addproduct'),
    path('register/',views.register,name='register'),
    path('logout/',view=views.userlogout,name='logout')
]