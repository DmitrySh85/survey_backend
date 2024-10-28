from django.http import HttpRequest

from .filters import EmployeesFilters
from .models import Employee


def get_filtered_employees(filters: EmployeesFilters):
    queryset = Employee.objects.all()
    if filters.tg_id:
        queryset = queryset.filter(tg_id=filters.tg_id)
    if filters.is_blocked:
        queryset = queryset.filter(is_blocked=filters.is_blocked)
    if filters.role:
        queryset = queryset.filter(role=filters.role)
    return queryset


def get_filters_from_employees_request(request: HttpRequest) -> EmployeesFilters:
    tg_id = request.query_params.get("tg_id")
    is_blocked = request.query_params.get("is_blocked")
    role = request.query_params.get("role")
    filters = EmployeesFilters(
        tg_id=tg_id,
        is_blocked=is_blocked,
        role=role
    )
    return filters