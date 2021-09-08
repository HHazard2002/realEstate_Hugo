from .models import Asset, Owner, Tenant
from django.contrib import admin

# Register your models here.

admin.site.register(Tenant),
admin.site.register(Owner),
admin.site.register(Asset),