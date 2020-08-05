from django.contrib import admin
from .models import AdminModel
from .models import PizzaModel
from .models import CustomerModel


admin.site.register(AdminModel)
admin.site.register(PizzaModel)
admin.site.register(CustomerModel)
