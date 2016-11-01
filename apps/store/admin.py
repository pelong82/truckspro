from django.contrib import admin
from apps.store.models import Client
from apps.store.models import Address
from apps.store.models import Cause
from apps.store.models import Order
from apps.store.models import ProcessOrder
from apps.store.models import Tire


# Register your models here.
admin.site.register(Client)
admin.site.register(Address)
admin.site.register(Cause)
admin.site.register(Order)
admin.site.register(ProcessOrder)
admin.site.register(Tire)