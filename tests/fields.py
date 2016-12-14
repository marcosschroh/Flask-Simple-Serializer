from unittest import TestCase

from flask_simple_serializer.serializers import Serializer
from flask_simple_serializer.fields import EmailField


class EmailFieldTest(TestCase):
    class EmailSerializer(Serializer):
        email = EmailField()

    def test(self):
        serializer = self.EmailSerializer({"email": "test@test.com"})
        self.assertEqual(serializer.email.data, "test@test.com")
        self.assertEqual(serializer.is_valid(), True)
        self.assertEqual(serializer.errors, dict())

        serializer = self.EmailSerializer({"email": "test"})
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(serializer.errors, {'email': ['Invalid email address.']})
