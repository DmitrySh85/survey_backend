from django.urls import path
from .views import EmployeeViewSet, UpdateEmployeeAPIView


urlpatterns = [
    path("<pk>/", UpdateEmployeeAPIView.as_view()),
    path("", EmployeeViewSet.as_view(
        {
            "get": "list",
            "post": "create"
        }
    )),
]
