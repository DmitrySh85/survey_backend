from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from ..models import Order, Item
from employees.models import Employee


User = get_user_model()


class CreateOrderAPIViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@test.com",
            username="test_user",
            password="test_password"
            )
        self.client = APIClient()
        self.url = "/api/store/order/"

        self.item = Item.objects.create(
            price=1,
            name="test item",
            description="test item description"
        )
        self.employee = Employee.objects.create(
            name="John Doe",
            tg_id=11111111111,
            points=1
        )

    def test_success(self):
        self.client.force_authenticate(user=self.user)
        payload = {
            "purchaser": self.employee.id,
            "item": self.item.id
        }
        response = self.client.post(
            path=self.url, data=payload, format="json"
        )
        orders_count = Order.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(orders_count, 1)

    def test_error_insufficient_points(self):
        self.item.price = 100
        self.item.save()
        self.client.force_authenticate(user=self.user)
        payload = {
            "purchaser": self.employee.id,
            "item": self.item.id
        }
        response = self.client.post(
            path=self.url, data=payload, format="json"
        )
        orders_count = Order.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(orders_count, 0)
        self.assertEqual(self.employee.points, 1)

    def test_error_no_item_exists(self):
        self.client.force_authenticate(user=self.user)
        payload = {
            "purchaser": self.employee.id,
            "item": 1000
        }
        response = self.client.post(
            path=self.url, data=payload, format="json"
        )
        orders_count = Order.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(orders_count, 0)
        self.assertEqual(self.employee.points, 1)

    def test_error_no_purchaser_exists(self):
        self.client.force_authenticate(user=self.user)
        payload = {
            "purchaser": "1d0ccc17-cdf1-404f-a3be-1912705d732b",
            "item": self.item.id
        }
        response = self.client.post(
            path=self.url, data=payload, format="json"
        )
        orders_count = Order.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(orders_count, 0)
        self.assertEqual(self.employee.points, 1)

    def test_error_missed_field(self):
        self.client.force_authenticate(user=self.user)
        payload = {
            "purchaser": self.employee.id,
        }
        response = self.client.post(
            path=self.url, data=payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_error_unauthorized(self):
        payload = {
            "purchaser": self.employee.id,
            "item": self.item.id
        }
        response = self.client.post(
            path=self.url, data=payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)






