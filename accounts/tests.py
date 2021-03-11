from django.test import TestCase
from django.contrib.auth import get_user_model

class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='user@domain.com', 
            password='foo'
        )
        self.assertEqual(user.email, 'user@domain.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_staff)
        
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='superuser@domain.com',
            password='foo'
        )
        self.assertEqual(admin_user.email, 'superuser@domain.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_admin)
        self.assertTrue(admin_user.is_staff)