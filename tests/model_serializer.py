from unittest import TestCase

import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


from flask_simple_serializer import ModelSerializer


class ModelSerializerTest(TestCase):

    def setUp(self):
        self.base = declarative_base()
        self.init_model()
        self.init_model_serializer()

    def tearDown(self):
        self.model = None
        self.model_serializer = None

    def init_model(self, type_=sa.Unicode(255), **kwargs):
        kwargs.setdefault('nullable', False)

        class TestModel(self.base):
            __tablename__ = 'test_model'
            id = sa.Column(sa.Integer, primary_key=True)
            first_name = sa.Column(sa.String, nullable=False)
            age = sa.Column(sa.Integer, nullable=False)

        self.model = TestModel

    def init_model_serializer(self):
        class ModelSerializerTest(ModelSerializer):
            class Meta:
                model = self.model

        self.model_serializer = ModelSerializerTest

    @staticmethod
    def valid_data():
        return {"age": 10, "first_name": "Bob"}

    @staticmethod
    def invalid_data():
        return {"age": "Hallo"}

    def test_data(self):
        serializer = self.model_serializer(self.valid_data())

        if serializer.is_valid():
            self.assertEqual(serializer.age.data, 10)
            self.assertEqual(serializer.first_name.data, 'Bob')
            self.assertEqual(serializer.data, {'age': 10, 'first_name': 'Bob'})

    def test_is_valid(self):
        serializer = self.model_serializer(self.valid_data())
        self.assertEqual(serializer.is_valid(), True)

        serializer = self.model_serializer(self.invalid_data())
        self.assertEqual(serializer.is_valid(), False)

    def test_errors(self):
        serializer = self.model_serializer(self.invalid_data())

        serializer.is_valid()
        self.assertEqual(serializer.errors, {
            'first_name': ['This field is required.'],
            'age': ['Not a valid integer value']
        })

    def test_not_errors(self):
        serializer = self.model_serializer(self.valid_data())

        if serializer.is_valid():
            self.assertEqual(serializer.errors, dict())

    def test_errors_before_is_valid(self):
        # Should call .is_valid() before call .errors
        serializer = self.model_serializer(self.valid_data())

        with self.assertRaises(AssertionError):
            serializer.errors

    def test_data_before_is_valid(self):
        # Should call .is_valid() before call .errors
        serializer = self.model_serializer(self.valid_data())

        with self.assertRaises(AssertionError):
            serializer.data
