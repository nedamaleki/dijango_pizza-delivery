from django.contrib import admin
from .models import AdminModel
from .models import PizzaModel
from .models import CustomerModel
from .models import OrderModel


admin.site.register(AdminModel)
admin.site.register(PizzaModel)
admin.site.register(CustomerModel)
admin.site.register(OrderModel)

