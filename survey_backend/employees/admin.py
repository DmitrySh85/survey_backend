from django.contrib import admin

from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["tg_id", "name", "role", "created_at", "is_blocked"]
    list_display_links = ["name",]
    list_filter = ["name", "created_at"]
    list_editable = ["is_blocked"]


admin.site.register(Employee, EmployeeAdmin)
