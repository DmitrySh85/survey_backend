from django.contrib import admin
from .models import Item, Order


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    list_display_links = ['name']
    list_editable = ['price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ["item", "purchaser", "status"]
    list_display_links = ["item", "purchaser"]
    list_editable = ["status"]


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)