from django.test import TestCase
from django.urls import reverse
from account.models import Account

class RegistrationFormTest(TestCase):
    def setUp(self):
        self.registration_url = reverse('register')

    def test_registration_form_valid_data(self):
        data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password1': 'securepassword',
            'password2': 'securepassword',
        }
        response = self.client.post(self.registration_url, data)
        self.assertEqual(response.status_code, 302)  # Sprawdź, czy przekierowuje po pomyślnej rejestracji

        # Sprawdzanie czy uzytkownik utworzył się
        user_exists = Account.objects.filter(username=data['username']).exists()
        self.assertTrue(user_exists)

    def test_registration_form_invalid_data(self):
        data = {
            'email': 'invalid_email',
            'username': '',  # Pusty username
            'password1': 'password',
            'password2': 'different_password',
        }
        response = self.client.post(self.registration_url, data)
        self.assertEqual(response.status_code, 200)

        # Sprawdzanie czy formularz zawiera błędy
        self.assertContains(response, 'Enter a valid email address.')
        self.assertContains(response, 'This field is required.')
        self.assertContains(response, 'The two password fields didn’t match.')

    def test_registration_form_password_mismatch(self):
        data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password1': 'securepassword',
            'password2': 'different_password',
        }
        response = self.client.post(self.registration_url, data)
        self.assertEqual(response.status_code, 200) 

        self.assertContains(response, 'The two password fields didn’t match.')