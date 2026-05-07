from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import CustomUser, Staff, Course

class EditResultViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a course
        self.course = Course.objects.create(name="Test Course")
        # Create a staff user
        # Note: user_type is CharField, but signal compares with int.
        # Middleware compares with string. We use 2 and ensure profile exists.
        self.staff_user = CustomUser.objects.create_user(
            email="staff@test.com",
            password="password123",
            user_type=2,
            first_name="Staff",
            last_name="User"
        )
        # The staff object should be created via signal, but we ensure it exists and has a course
        self.staff, created = Staff.objects.get_or_create(admin=self.staff_user)
        self.staff.course = self.course
        self.staff.save()

        # Log in
        self.client.login(email="staff@test.com", password="password123")

    def test_edit_result_post_invalid_form(self):
        url = reverse('edit_student_result')
        # Send POST with missing data to trigger form.is_valid() == False
        # EditResultForm requires session_year, subject, student, test, exam
        response = self.client.post(url, {})

        # Check response status
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is rendered
        self.assertTemplateUsed(response, "staff_template/edit_student_result.html")

        # Check that the warning message is present
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(m.message == "Result Could Not Be Updated" for m in messages))
        self.assertTrue(any(m.level_tag == "warning" for m in messages))

    def test_edit_result_post_invalid_data_types(self):
        url = reverse('edit_student_result')
        # Send POST with invalid data types to trigger form.is_valid() == False
        response = self.client.post(url, {
            'session_year': 'invalid',
            'subject': 'invalid',
            'student': 'invalid',
            'test': 'not-a-number',
            'exam': -10
        })

        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(m.message == "Result Could Not Be Updated" for m in messages))
