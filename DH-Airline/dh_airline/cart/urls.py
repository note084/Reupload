from django.urls import include, path, re_path
from django.conf.urls import url
from . import views
from .views import (
    add_to_cart,
    order_details,
    CartPage,
)

app_name = 'cart'

urlpatterns = [
    path('', CartPage.as_view(), name='cartpage'),
    path('', views.PaymentPage.as_view(),name='payment'),
    path('add-to-cart/<item_id>/', add_to_cart, name="add_to_cart"),
    url(r'^order-summary/$', order_details, name="cart_summary"),
    #url(r'^success/$', success, name='purchase_success'),
    #url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    #url(r'^checkout/$', checkout, name='checkout'),
    #url(r'^update-transaction/(?P<token>[-\w]+)/$', update_transaction_records,
    #    name='update_records')
]
