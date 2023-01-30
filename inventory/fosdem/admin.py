from django.contrib import admin
from .models import Box, Item, Location, Inventory, Transport

# Register your models here.
admin.site.register(Box)
admin.site.register(Item)
admin.site.register(Location)
admin.site.register(Inventory)
admin.site.register(Transport)
