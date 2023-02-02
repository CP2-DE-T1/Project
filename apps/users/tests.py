from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from .models import User
from rest_framework import status
# Create your tests here.

#ref:https://velog.io/@migdracios/DRF-DRF-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%BD%94%EB%93%9C-%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0
class TestUsersApp(APITestCase):
    def sign_up_test(self):
        self.test_user={
            'username':'tester',
            'name':'tester_name',
            'email':'tester@django.com',
            'password':'sample1111',
            'password_check':'sample1111',
            'gender':'Female',
            'birth_date':'1950-05-05',
        }

        self.signup_url = '/api/users/sign-up/'
        self.response = self.client.post(self.signup_url, data=self.test_user)
        self.assertEqual(self.response.status_code, status.HTTP_201_Created)

    def setUp(self):
        self.data ={
            'username':'test12',
            'name':'test12',
            'email':'test12@django.com',
            'password':'sample1111',
            'password_check':'sample1111',
            'gender':'Female',
            'birth_date':'2000-01-01',
        }