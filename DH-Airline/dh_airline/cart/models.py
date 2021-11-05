from django.db import models
from django.contrib.auth.models import User

from accounts.models import Account
from flights.models import Flight
# Create your models here.

class OrderItem(models.Model):
    flight = models.OneToOneField(Flight, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    dated_ordered = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.flight.origin

class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    #payment_details = models.ForeignKey(Payment, null=True)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)


""" @login_required()
def add_to_cart(request, **kwargs):
    #gets user profile
    user_profile = get_object_or_404(Account, user=request.user)
    flight = Flight.objects.filter(id=kwargs.get('pk', "")).first()
    if flight in request.user.profile.Flight.all():
        messages.info(request, 'This item is already in your cart')
        return redirect(reverse('cart:cart-list'))

    #create orderItem of the selected flight
    order_item, status = OrderItem.objects.get_or_create(flight=flight)
    #create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered)
    user_order.items.add(order_item)

    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()

    messages.info(request, "item added to cart")
    return redirect(reverse('cart:cart-list')) """