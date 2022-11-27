from django.contrib import admin

# Register your models here.
from .models import Event, Player
admin.site.register(Event)
admin.site.register(Player)