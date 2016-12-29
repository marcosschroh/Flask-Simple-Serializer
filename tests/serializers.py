from unittest import TestCase

from flask_simple_serializer.serializers import BaseSerializer, Serializer
from flask_simple_serializer import StringField, BooleanField, EmailField, validators


#class BaseSerialazerTest(TestCase):

#    def test_empty_data(self):
        # Can instanciate a serializer with empty data
#        with self.assertRaises(ValueError):
#            BaseSerializer()


class SerializerTest(TestCase):

    class Userserializer(Serializer):
        username = StringField('Username')
        email = EmailField('Email Address', [validators.Length(min=4, max=25)])
        accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])

    @staticmethod
    def valid_data():
        return {"username": "Bob", "email": "bob@gmail.com", "accept_rules": True}

    @staticmethod
    def invalid_data():
        return {"username": "Bob", "email": "bob@gmail.com"}

    def test_is_valid(self):
        serializer = self.Userserializer(self.valid_data())
        self.assertEqual(serializer.is_valid(), True)

        serializer = self.Userserializer(self.invalid_data())
        self.assertEqual(serializer.is_valid(), False)

    def test_data(self):
        serializer = self.Userserializer(self.valid_data())

        if serializer.is_valid():
            self.assertEqual(serializer.username.data, 'Bob')
            self.assertEqual(serializer.email.data, 'bob@gmail.com')
            self.assertEqual(serializer.accept_rules.data, True)
            self.assertEqual(serializer.data, { 'username': 'Bob', 'accept_rules': True, 'email': 'bob@gmail.com'})

    def test_not_errors(self):
        serializer = self.Userserializer(self.valid_data())

        if serializer.is_valid():
            self.assertEqual(serializer.errors, dict())

    def test_errors(self):
        serializer = self.Userserializer(self.invalid_data())

        serializer.is_valid()
        self.assertEqual(serializer.errors, {'accept_rules': ['This field is required.']})

    def test_errors_before_is_valid(self):
        # Should call .is_valid() before call .errors
        serializer = self.Userserializer(self.valid_data())

        with self.assertRaises(AssertionError):
            serializer.errors

    def test_data_before_is_valid(self):
        # Should call .is_valid() before call .errors
        serializer = self.Userserializer(self.valid_data())

        with self.assertRaises(AssertionError):
            serializer.data

