from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Table, Orders


admin.site.register(Table)
admin.site.register(Orders)