from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, {'page': 0}, name='home'),
    path('/home/<int:page>', views.home, name='home'),
    path('/home/', views.home, {'page': 0}, name='home'),
    path('/products/<str:ruta>', views.products, name='products'),
    path('/search/', views.search, name='search'),
]
