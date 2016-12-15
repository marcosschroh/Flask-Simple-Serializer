"""
Flask-Simple-Serializer
=======
Flask-Rest-Serializers has Serializers to validate data in a API
and rendering. It ise WTForms and cool ideas from Django-Rest-Framework

:copyright: Copyright (c) 2010 by Marcos Schroh.
:license: BSD, see LICENSE.txt for details.
"""
from wtforms import validators, widgets
from wtforms.fields import *
from wtforms.validators import ValidationError

from .fields import EmailField
from .serializers import Serializer, ModelSerializer


__version__ = '1.0'
