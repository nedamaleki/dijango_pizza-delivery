from django.contrib import admin
from .models import AdminModel
from .models import PizzaModel


admin.site.register(AdminModel)
admin.site.register(PizzaModel)
