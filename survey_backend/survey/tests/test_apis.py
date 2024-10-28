from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from ..models import Question


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
