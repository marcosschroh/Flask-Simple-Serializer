import six

from werkzeug.datastructures import MultiDict
from collections import OrderedDict

from wtforms.form import Form
from wtforms_alchemy import ModelForm


def serializer_factory(base=Form):

    class BaseSerializer(base):

        def __init__(self, data_dict=None, model_instance=None, **kwargs):
            # Supouse that the data is already a Python Dict
            self._validate_called = None
            self.model_instance = model_instance
            self.formdata = MultiDict({})

            if data_dict:
                if not isinstance(data_dict, dict):
                    raise ValueError("Data must be a Dict instance")
                self.formdata = MultiDict(data_dict)

            super(BaseSerializer, self).__init__(formdata=self.formdata, **kwargs)

        def is_valid(self):
            self._validate_called = True
            return super(BaseSerializer, self).validate()

        @property
        def data(self):
            if not self._validate_called:
                msg = 'You must call `.is_valid()` before accessing `.data`.'
                raise AssertionError(msg)
            return super(BaseSerializer, self).data

        def validate(self):
            raise NotImplementedError

        @property
        def errors(self):
            if not self._validate_called:
                msg = 'You must call `.is_valid()` before accessing `.errors`.'
                raise AssertionError(msg)
            return super(BaseSerializer, self).errors

    return BaseSerializer


BaseSerializer = serializer_factory()
ModelBaseSerilizer = serializer_factory(base=ModelForm)


class SerializerMetaclass(type):
    """
    This metaclass sets a dictionary named `_declared_fields` on the class.
    Any instances of `Field` included as attributes on either the class
    or on any of its superclasses will be include in the
    `_declared_fields` dictionary.
    """

    @classmethod
    def _get_declared_fields(cls, bases, attrs):
        fields = [(field_name, attrs.pop(field_name))
                  for field_name, obj in list(attrs.items())
                  if isinstance(obj, dict)]
        fields.sort(key=lambda x: x[1]._creation_counter)

        # If this class is subclassing another Serializer, add that Serializer's
        # fields.  Note that we loop over the bases in *reverse*. This is necessary
        # in order to maintain the correct order of fields.
        for base in reversed(bases):
            if hasattr(base, '_declared_fields'):
                fields = list(base._declared_fields.items()) + fields

        return OrderedDict(fields)

    def __new__(cls, name, bases, attrs):
        attrs['_declared_fields'] = cls._get_declared_fields(bases, attrs)
        return super(SerializerMetaclass, cls).__new__(cls, name, bases, attrs)


class Serializer(BaseSerializer):
    pass


class ModelSerializer(ModelBaseSerilizer):
    pass
