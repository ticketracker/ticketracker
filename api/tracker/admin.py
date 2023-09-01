from django.contrib import admin
from .models import Tracker, TicketRequest, Provider


admin.site.register(Tracker)
admin.site.register(TicketRequest)
admin.site.register(Provider)