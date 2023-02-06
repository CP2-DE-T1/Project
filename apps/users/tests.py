from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from .models import User
from rest_framework import status
# Create your tests here.

#ref:https://velog.io/@migdracios/DRF-DRF-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%BD%94%EB%93%9C-%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0
class TestUsersApp(APITestCase):
    # 각각 test method 실행시 마다 실행됨
    # setUpTestData()는 테스트 시작할때 딱한번 실행됨
    def setUp(self):
        self.user ={
            'username':'test12',
            'name':'test12',
            'email':'test12@django.com',
            'password':'sample1111',
            'password_check':'sample1111',
            'gender':'Female',
            'birth_date':'2000-01-01',
        }
        self.user.save()
    
    #회원가입 test
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
    
    # 비밀번호 확인 test
    def sign_up_validation_password(self):
        self.test_user={
            'username':'tester',
            'name':'tester_name',
            'email':'tester@django.com',
            'password':'sample2222',
            'password_check':'sample1111',
            'gender':'Female',
            'birth_date':'1950-05-05',
        }

        self.signup_url = '/api/users/sign-up/'
        self.response = self.client.post(self.signup_url, data=self.test_user)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    #아이디 중복 방지 test
    def sign_up_validation_duplicated_user_name(self):
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
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    # 로그인 test(성공)
    def sign_in_test(self):
        self.data={
            'username':'test12',
            'passwor':'sample1111',
        }

        self.signin_url='/api/users/sign-in'
        self.response=self.client.post(self.signin_url, data=self.data, format='json')
        self.asserEqual(self.response.status_code, status.HTTP_200_OK)

    # 로그인 test(실패)
    def sign_in_test_fail(self):
        self.data={
            'username':'test12',
            'passwor':'sample2222',
        }

        self.signin_url='/api/users/sign-in'
        self.response=self.client.post(self.signin_url, data=self.data, format='json')
        self.asserEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)