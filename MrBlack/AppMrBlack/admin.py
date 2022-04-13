from django.contrib import admin
from .models import Hamburguesas, Locales, Panchos

# Register your models here.
admin.site.register(Locales)
admin.site.register(Hamburguesas)
admin.site.register(Panchos)

