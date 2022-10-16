from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone


def validate_stock(value):
    if 0 < value < 1000:
        return value
    else:
        raise ValidationError("This field accepts value between 0 and 1000")


class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    desc = models.TextField(blank=True)
    interested = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def topup(self):
        self.stock = self.stock + 200


class Client(User):
    CITY_CHOICES = [
        ('WD', 'Windsor'),
        ('TO', 'Toronto'),
        ('CH', 'Chatham'),
        ('WL', 'Waterloo'), ]
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')
    interested_in = models.ManyToManyField(Type)
    phoneNo = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class OrderItem(models.Model):
    STATUS_CHOICES = [
        ('0', 'Cancelled'),
        ('1', 'Placed'),
        ('2', 'Shipped'),
        ('3', 'Delivered'), ]
    item = models.ForeignKey(
        Item, related_name='orderItems', on_delete=models.CASCADE)
    client = models.ForeignKey(
        Client, related_name='clientOrderedItems', on_delete=models.CASCADE)
    numberOfItems = models.IntegerField(default=1)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.item.name

    def total_price(self):
        return self.numberOfItems * Item.price
