from django.test import TestCase
import json
from rest_framework import status
from django.test import Client
from django.urls import reverse
from .models import User

# Create your tests here.

client = Client()


class UserTest(TestCase):

    def setUp(self):
        User.objects.create(
            name='oscar', password="passwor3weweqr", email='Gradane@pepe.com')
        User.objects.create(
            name='manuel', password="12345678", email='Gradansse@pepe2.com')

    def test_user_name(self):
        user_manuel = User.objects.get(name='manuel')
        user_oscar = User.objects.get(name='oscar')
        self.assertEqual(
            user_manuel.name, "manuel")
        self.assertEqual(
            user_oscar.name, "oscar")


class CreateNewUserTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            'name': 'manuel',
            'email': "manuel@gmail.com",
            'password': 'pass'
        }
        self.invalid_payload = {
            'name': 'oscar',
            'email': 4,
            'password': 'pass'
        }

    def test_create_valid_user(self):
        response = client.post(
            reverse('post_register'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = client.post(
            reverse('post_register'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
