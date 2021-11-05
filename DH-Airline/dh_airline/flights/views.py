from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, ListView, CreateView, DeleteView, DetailView
from .models import Flight
from cart.models import Order
from . import models
# Create your views here.

def search(request):
    try:
        orig = request.GET.get('origin')
        dest = request.GET.get('destination')
    except:
        orig = None
        dest = None
    if orig and dest:
        flights = Flight.objects.filter(origin=orig, destination=dest)
        context = {'dest' : dest, 'orig' : orig, 'flights': flights}
        template = 'flights/flight_list.html'
        if not flights:
            context = {'DNE' : 'Invalid Search'}
            template = 'bookpage.html/'
    elif orig:
        flights = Flight.objects.filter(origin=orig)
        context = {'orig' : orig, 'flights': flights}
        template = 'flights/flight_list.html'
        if not flights:
            context = {'DNE' : 'Invalid Search'}
            template = 'bookpage.html/'
    elif dest:
        flights = Flight.objects.filter(destination=dest)
        context = {'dest' : dest, 'flights': flights}
        template = 'flights/flight_list.html'
        if not flights:
            context = {'DNE' : 'Invalid Search'}
            template = 'bookpage.html/'
    else:
        template = 'bookpage.html/'
        context = {}
    return render(request, template, context)



class FlightDetailView(DetailView):
    context_object_name = 'flight_details'
    model = models.Flight
    template_name = 'flights/flight_detail.html'


class FlightListView(ListView):
    template_name = 'flights/flight_list.html'
    context_object_name = 'flights'
    model = models.Flight

class FlightCartView(ListView):
    template_name = 'cartpage.html'
    context_object_name = 'flight_item'
    model = models.FlightItems

class BookPage(TemplateView):
    template_name = 'bookpage.html'

class CreateItem(CreateView):
    fields = ("quantity", "price")
    model = models.FlightItems
    template_name = 'flights/flight_detail.html'

def add_flight(request):
    item = Flight.objects.filter(id=kwargs.get('pk')).first()
    flight_item, status = FlightItems.objects.get_or_create(item=item)
    return render(request, "cartpage.html", context)


@login_required
def flight_list(request):
    object_list = Flight.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
    	user_order = filtered_orders[0]
    	user_order_items = user_order.items.all()
    	current_order_products = [flight.flight for flight in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_products': current_order_products
    }

    return render(request, "cartpage.html", context)
