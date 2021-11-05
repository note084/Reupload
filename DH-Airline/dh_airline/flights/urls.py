from django.urls import path,re_path
from . import views
from cart.views import add_to_cart

app_name = 'flights'

urlpatterns = [
    path('', views.BookPage.as_view(), name='bookpage'),
    path('s/', views.search, name='search'),
    path('flight/<pk>/', views.FlightDetailView.as_view(), name='detailpage'),
    path('add/<pk>/', views.add_flight, name="add"),
    
]
