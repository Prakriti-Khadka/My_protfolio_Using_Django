from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date','desc')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('date',)
