from flask import Response as SimpleResponse
from flask import json

from .status_codes import HTTP_200_OK
from .serializers import BaseSerializer


class Response(SimpleResponse):

    def __init__(self, data, headers=None, status_code=HTTP_200_OK):
        """
        For now the content/type always will be application/json.
        We can change it to make a Web Browseable API
        """
        if isinstance(data, BaseSerializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.errors`. representation.'
            )
            raise AssertionError(msg)

        data = json.dumps(data)

        content_type = "application/json"

        super(Response, self).__init__(
            data, headers=None, content_type=content_type, status=status_code
        )
