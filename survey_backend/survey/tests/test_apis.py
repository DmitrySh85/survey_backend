from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from ..models import Question, DailySurveyCounter
from employees.models import Employee


User = get_user_model()


class QuestionListViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@test.com",
            username="test_user",
            password="test_password"
        )
        self.client = APIClient()
        self.url = "/api/survey/questions/"

    def create_questions(self):
        Question.objects.create(
            text="Test question text",
            first_answer="1",
            second_answer="2",
            third_answer="3",
            fourth_answer="4",
            valid_answer_number=1,
            description="test_decription"
        )
        Question.objects.create(
            text="Second Test question text",
            first_answer="1",
            second_answer="2",
            third_answer="3",
            fourth_answer="4",
            valid_answer_number=1,
            description="test_decription"
        )
        Question.objects.create(
            text="Third Test question text",
            first_answer="1",
            second_answer="2",
            third_answer="3",
            fourth_answer="4",
            valid_answer_number=1,
            description="test_decription"
        )

    def test_success(self):
        self.create_questions()
        self.client.force_authenticate(user=self.user)
        data = {"length": 2}
        response = self.client.get(self.url, data=data)
        self.assertEqual(len(response.data), data.get("length"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_error_unauthorized(self):
        self.create_questions()
        data = {"length": 2}
        response = self.client.get(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



class DailySurveyCounterCreateAPIViewTest(APITestCase):
    def setUp(self):

        self.user = User.objects.create(
            email="test@test.com",
            username="test_user",
            password="test_password"
        )
        self.employee = Employee.objects.create(
            tg_id=11111111111,
            name="Test Employee"
        )
        self.client = APIClient()
        self.url = "/api/survey/attempts/"

    def create_survey_counter(self):
        DailySurveyCounter.objects.create(employee=self.employee)

    def test_success(self):
        self.client.force_authenticate(user=self.user)
        payload = {"employee": self.employee.id}
        response = self.client.post(self.url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_error_not_unique(self):
        self.create_survey_counter()
        self.client.force_authenticate(user=self.user)
        payload = {"employee": self.employee.id}
        response = self.client.post(self.url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_error_unauthorized(self):
        payload = {"employee": self.employee.id}
        response = self.client.post(self.url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_error_invalid_method(self):
        self.client.force_authenticate(user=self.user)
        payload = {"employee": self.employee.id}
        response = self.client.put(self.url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class IncreaseDaylySurveyCounterAPIViewTest(APITestCase):

    def setUp(self):

        self.user = User.objects.create(
            email="test@test.com",
            username="test_user",
            password="test_password"
        )
        self.employee = Employee.objects.create(
            tg_id=11111111111,
            name="Test Employee"
        )
        self.attempts_counter = DailySurveyCounter.objects.create(employee=self.employee)
        self.client = APIClient()
        self.url = "/api/survey/attempts/increase/"

    def test_success(self):
        self.client.force_authenticate(user=self.user)
        payload = {"employee": self.employee.id}
        response = self.client.post(self.url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_error_unauthorized(self):
        payload = {"employee": self.employee.id}
        response = self.client.post(self.url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_error_invalid_method(self):
        self.client.force_authenticate(user=self.user)
        payload = {"employee": self.employee.id}
        response = self.client.delete(self.url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
