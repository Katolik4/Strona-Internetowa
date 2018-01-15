from django.contrib import admin
from .models import Urzadzenie, Gpio

admin.site.register(Urzadzenie)
admin.site.register(Gpio)

