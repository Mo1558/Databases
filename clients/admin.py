from django.contrib import admin

# Register your models here.
from . models import Client,Country

admin.site.register(Client)
admin.site.register(Country)