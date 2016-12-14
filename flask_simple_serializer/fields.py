from wtforms.validators import Email

from wtforms import StringField


class EmailField(StringField):

    def __init__(self, label='', validators=None, **kwargs):
        if validators:
            validators.append(Email())
        else:
            validators = [Email()]

        super(EmailField, self).__init__(label, validators, **kwargs)
