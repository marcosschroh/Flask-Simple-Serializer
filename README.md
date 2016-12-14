# Flask-Simple-Serializer


Simple Serializer to valid API request

### Usage
```python

# my_app.serializers.py
from flask_simple_serializer.serializers import Serializer
from flask_simple_serializer import StringField, BooleanField, EmailField, validators

class Userserializer(Serializer):
    username = StringField('Username')
    email = EmailField('Email Address', [validators.Length(min=4, max=25)])
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])
    
    def create_user(self):
        pass

# my_app.views.py
from flask_simple_serializer.response import Response
from flask_simple_serializer.status_code import HTTP_200_OK, HTTP_400_BAD_REQUEST

from my_app.serializes import Userserializer

@site.route('/some_route/')
def user_registration():
    serializer = UserSerializer(request.json)
    
    if serializer.is_valid()
        # Do something
        serializer.create_user()
        return Response(status_code=HTTP_200_OK)
    return Response(serializer.errors, status_code=HTTP_400_BAD_REQUEST)
```

### TODO
  - Model Serializer
  - Serializer that accept Model instance (SqlAlchemy) 
  - Improve Documentation
  - Custom Felds
  - Parse request decorators
  - Test for Response and Status Codes
