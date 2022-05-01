from django.contrib import admin
from .models import Avatar, Contacto, Hamburguesas, Locales

# Register your models here.
admin.site.register(Locales)
admin.site.register(Hamburguesas)
admin.site.register(Contacto)
admin.site.register(Avatar)
