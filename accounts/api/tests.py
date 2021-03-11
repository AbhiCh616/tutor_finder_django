from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from accounts.models import User

class AccountsTest(APITestCase):
    def setUp(self):
        # Create a user
        self.test_user = User.objects.create_user(
             'test@example.com', 
             'testpassword'
        )

        # URL for creating account
        self.create_url = reverse('create')

        self.login_url = reverse('login')
    
    def test_create_user(self):
        data = {
            'email': 'example@domain.com',
            'password': 'randompassword'
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)
        self.assertTrue('token' in response.data)

    def test_login_user(self):
        create_data = {
            'email': 'example2@domain.com',
            'password': 'randompassword'
        }

        create_response = self.client.post(self.create_url, create_data, format='json')

        login_data = {
            'username': 'example2@domain.com',
            'password': 'randompassword'
        }

        login_response = self.client.post(self.login_url, login_data, format='json')

        self.assertTrue(create_response.data['token'], login_response.data['token'])