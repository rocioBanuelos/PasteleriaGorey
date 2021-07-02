from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.site_header = "Gorey Empleados | Administración"
admin.site.site_title = "Administración"
admin.site.index_title = "Gorey"

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(ProductTypes)
admin.site.register(Cake)
admin.site.register(Client)
admin.site.register(Buy)
admin.site.register(ItemsBuy)