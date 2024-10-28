from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from ..models import Employee


User = get_user_model()


class EmployeeViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@test.com",
            username="test_user",
            password="test_password"
        )
        self.client = APIClient()
        self.url = "/api/employees/"

    def create_employee(self):
        Employee.objects.create(
            tg_id=11111111111,
            name="Test Employee"
        )
    def create_employees(self):
        Employee.objects.create(
            tg_id=11111111111,
            name="Test Employee"
        )
        Employee.objects.create(
            tg_id=222222222222,
            name="Test Admin Employee",
            role="ADMIN"
        )
        Employee.objects.create(
            tg_id=333333333333,
            name="Test Blocked Employee",
            is_blocked=True
        )


    def test_create_success(self):
        self.client.force_authenticate(user=self.user)
        payload = {
            "tg_id": 11111111111,
            "name": "Test Employee"
        }
        response = self.client.post(path=self.url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_error_not_unique_tg_id(self):
        self.create_employee()
        self.client.force_authenticate(user=self.user)
        payload = {
            "tg_id": 11111111111,
            "name": "Test Employee"
        }
        response = self.client.post(path=self.url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_error_unauthorized(self):
        payload = {
            "tg_id": 11111111111,
            "name": "Test Employee"
        }
        response = self.client.post(path=self.url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_error_invalid_method(self):

        self.client.force_authenticate(user=self.user)
        payload = {
            "tg_id": 11111111111,
            "name": "Test Employee"
        }
        response = self.client.patch(path=self.url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_list_success(self):
        self.create_employees()
        self.client.force_authenticate(user=self.user)
        response = self.client.get(path=self.url)
        count = response.data.get("count")
        employee_db_count = Employee.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(count, employee_db_count)

    def test_list_success_is_blocked(self):
        self.create_employees()
        data = {"is_blocked": True}
        self.client.force_authenticate(user=self.user)
        response = self.client.get(path=self.url, data=data)
        count = response.data.get("count")
        employee_db_count = Employee.objects.filter(is_blocked=True).count()
        self.assertNotEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(count, employee_db_count)

    def test_success_is_admin(self):
        self.create_employees()
        data = {"role": "ADMIN"}
        self.client.force_authenticate(user=self.user)
        response = self.client.get(path=self.url, data=data)
        count = response.data.get("count")
        employee_db_count = Employee.objects.filter(role="ADMIN").count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(count, 0)
        self.assertEqual(count, employee_db_count)

    def test_success_is_not_admin(self):
        self.create_employees()
        data = {"role": "MASTER"}
        self.client.force_authenticate(user=self.user)
        response = self.client.get(path=self.url, data=data)
        count = response.data.get("count")
        employee_db_count = Employee.objects.filter(role="MASTER").count()
        self.assertNotEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(count, employee_db_count)