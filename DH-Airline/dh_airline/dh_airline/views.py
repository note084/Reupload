from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, CreateView, DeleteView
# Create your views here.
from flights import models

class HomePage(TemplateView):
    template_name='homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[''] = 'text'
        return context


class MyTripsPage(TemplateView):
    template_name = 'mytrips.html'

class LogIn(TemplateView):
    template_name = 'login.html'

class LogOut(TemplateView):
    template_name = 'logout.html'

class BookPage(TemplateView):
    template_name = 'bookpage.html'

class SupportPage(TemplateView):
	template_name = 'support.html'

class CheckOutPage(TemplateView):
    template_name = 'checkout.html'

class ConfirmationPage(TemplateView):
    template_name = 'confirmation.html'

class MyTripsPage(TemplateView):
    template_name = 'myTrips.html'

class MyTripsConfirmation(TemplateView):
    template_name = "MyTripsConfirmation.html"

class ManagerReport(ListView):
    model = models.Flight
    context_object_name = 'flights'
    template_name = 'managerreport.html'
