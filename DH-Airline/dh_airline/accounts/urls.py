# April 16, 2020
# Kyle Ear
# Gerardo Pena
from django.urls import include, path
from django.contrib.auth import views as auth_views
from accounts.views import signup_view, account_view

app_name='accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    # call loginview from auth_view  template_name is what we wanna connect to
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/', signup_view, name='signup'),
    path('account/', account_view, name='account'),
]
