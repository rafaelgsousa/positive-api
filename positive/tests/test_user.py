from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class UserTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        client = APIClient()
        new_user = {
            "email": "teste@email.com",
            "phone": "+5508691111119",
            "name": "teste",
            "type_account": "Free",
            "password": "senha001"
        }
        response = client.post('/positive/user/', new_user, format='json')
        cls.user = response.data

    def setUp(self):
        self.client = APIClient()
        
        self.new_user_login = {
                    "email": "teste@email.com",
                    "password": "senha001"
                }
        
        self.new_user_login_password_error = {
                    "email": "teste@email.com",
                    "password": "senha005"
                }
        
        self.new_outher_user_login = {
                    "email": "teste2@email.com",
                    "password": "senha001"
                }
        
        self.new_outher = {
                    "email": "teste2@email.com",
                    "phone": "+55086911111122",
                    "name": "teste2",
                    "type_account": "Free",
                    "password": "senha001"
                }

    def test_create_user(self):

            response = self.client.post('/positive/user/', self.new_outher, format='json')

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_before_user_create(self):
        response = self.client.post('/positive/user/login/', self.new_user_login, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_user(self):
        user = self.client.post('/positive/user/', self.new_outher, format='json')

        login = self.client.post('/positive/user/login/', self.new_outher_user_login, format='json')

        token = login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.get(f'/positive/user/{login.data['user']['id']}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_user_error(self):
        response = self.client.post('/positive/user/login/', self.new_user_login_password_error, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user_error_three_times(self):
        self.client.post('/positive/user/login/', self.new_user_login_password_error, format='json')

        self.client.post('/positive/user/login/', self.new_user_login_password_error, format='json')

        self.client.post('/positive/user/login/', self.new_user_login_password_error, format='json')

        response = self.client.post('/positive/user/login/', self.new_user_login_password_error, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)