"""softwareproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomePage.as_view()),
    path('home/', views.HomePage.as_view(), name='homepage'),
    path('mytrips/', views.MyTripsPage.as_view(), name='reservepage'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
    path('book/', include("flights.urls", namespace="book")),
    path('cart/', include("cart.urls", namespace='cartpage')),
    path('checkout/', views.CheckOutPage.as_view(), name = 'checkout'),
    path('confirmation/', views.ConfirmationPage.as_view(), name = 'confirmation'),
    path('mytrips/', views.MyTripsPage.as_view(), name = 'mytrips'),
    path('mytripsconfirmation/', views.MyTripsConfirmation.as_view(), name = 'mytripsconfirmation'),
    path('report/', views.ManagerReport.as_view(), name = 'managerreport')

]
