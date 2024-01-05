from django.contrib import admin

# Register your models here.
from .models import Drinks
from .models import DrinksCategory

admin.site.register(Drinks)
admin.site.register(DrinksCategory)
