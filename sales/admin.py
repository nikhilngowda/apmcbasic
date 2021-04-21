from django.contrib import admin
from .models import Sales, Agent, FirmUser
# Register your models here.

class SalesAdmin(admin.ModelAdmin):
    list_display=('amount', 'description', 'agent', 'date')
    search_fields=('amount', 'description', 'agent', 'date')
    list_per_page=10


admin.site.register(Sales)
admin.site.register(Agent)
admin.site.register(FirmUser)
