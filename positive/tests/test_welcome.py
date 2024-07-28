import os

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import CustomUser, Welcome


class UserTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        base_dir = os.path.dirname(__file__)
        image_path = os.path.join(base_dir, 'media_to_test', 'geek-avatar-1632962.jpg')
        video_path = os.path.join(base_dir, 'media_to_test', '2024-02-27 16-48-29.mp4')

        self.super_user = CustomUser.objects.create(**{
            "email": "teste@email.com",
            "phone": "+5508691111119",
            "first_name": "teste",
            "type_account": "Free",
            "password": "senha001",
            "is_superuser": True
        })

        self.super_user_login = {
                    "email": "teste@email.com",
                    "password": "senha001"
                }

        self.welcome = {
            'title': 'Welcome Title',
            'cover': (open(image_path, 'rb'), 'geek-avatar-1632962.jpg', 'image/jpeg'),
            'video': (open(video_path, 'rb'), '2024-02-27 16-48-29.mp4', 'video/mp4'),
            'description': 'Welcome Description',
        }

    def test_create_one_welcome_data(self):
        login = self.client.post('/positive/user/login/', self.super_user_login, format='json')

        token = login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.post(f'/positive/welcome/', self.welcome, format='multipart')

        print(f'Response = {response.data}')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


