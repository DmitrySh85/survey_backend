from rest_framework.generics import UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer
from .services import (
    get_filtered_employees,
    get_filters_from_employees_request
)


class EmployeePagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 1000


class EmployeeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination

    def get_queryset(self):
        filters = get_filters_from_employees_request(self.request)
        queryset = get_filtered_employees(filters)
        return queryset


class UpdateEmployeeAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
