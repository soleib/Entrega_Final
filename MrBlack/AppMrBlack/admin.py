from django.contrib import admin
from .models import Avatar, Hamburguesas, Locales, Panchos

# Register your models here.
admin.site.register(Locales)
admin.site.register(Hamburguesas)
admin.site.register(Panchos)
admin.site.register(Avatar)
