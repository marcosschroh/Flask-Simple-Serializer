from werkzeug.datastructures import MultiDict

from wtforms.form import Form
from wtforms_alchemy import ModelForm


def serializer_factory(base=Form):

    class BaseSerializer(base):

        def __init__(self, data_dict=None, **kwargs):
            # Supouse that the data is already a Python Dict
            self.validate_called = None

            if not data_dict:
                raise ValueError("Data must be supplied")

            self.formdata = MultiDict(data_dict)

            try:
                # This section will be used to validate a json
                self.request_data = data_dict
            except Exception as e:
                print(e)
                raise ValueError("Invalid json")

            super(BaseSerializer, self).__init__(formdata=self.formdata, **kwargs)

        def is_valid(self):
            self.validate_called = True
            return super(BaseSerializer, self).validate()

        def validate(self):
            raise NotImplementedError

        @property
        def errors(self):
            if not self.validate_called:
                msg = 'You must call `.is_valid()` before accessing `.errors`.'
                raise AssertionError(msg)
            return super(BaseSerializer, self).errors

    return BaseSerializer


BaseSerializer = serializer_factory()
ModelBaseSerilizer = serializer_factory(base=ModelForm)


class Serializer(BaseSerializer):
    pass


class ModelSerializer(ModelBaseSerilizer):
    pass
