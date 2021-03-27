from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()

class LectureUserTestCase(TestCase):

    def setUp(self):
        user = User(username='test')
        user.is_staff = True
        user.is_superuser = True
        user.set_password('Passord123')
        user.save()

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertGreaterEqual(user_count,1)
    
    def test_user_password(self):
        user_qs = User.objects.filter(username__iexact='test')
        self.assertTrue(
            user_qs[0].check_password('Passord123')
            )


        