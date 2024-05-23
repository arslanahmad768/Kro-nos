from apps.authentication.models import User
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError
from rest_framework import status
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response


import jwt
import os

class RequestMiddleware:
    """
    Middleware to get request data and access it from methods
    which have no direct access to 'request' object
    """
    _request = None
    _HOST = 'VIRTUAL_HOST'

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        RequestMiddleware._request = self.update_request(request)
        return self.get_response(request)

    def update_request(self, request):
        """Getting None in request.user inside django-auditlog middleware, let's try
        fiddling with the request!"""

        try:
            token = get_authorization_header(request).decode('utf-8').split(" ")[1]
            if token is None or token == "null" or token.strip() == "":
                print("We are missing token!")
            else:
                decoded = jwt.decode(token, settings.SECRET_KEY)
                request.user = User.objects.get_by_natural_key(decoded['username'])
        except ExpiredSignatureError:
            return Response(data={"status": "error", "message": "token expired"}, status=status.HTTP_401_UNAUTHORIZED)
        except IndexError as e:
            print("seems like no token in the request header")

        return request


    @classmethod
    def get_scheme(cls):
        return cls._request.scheme or 'http'  # http is fallback-default

    @classmethod
    def get_base_url(cls):
        return f'{cls._request.scheme}://{os.getenv(_HOST, cls._request.get_host())}'

    @classmethod
    def get_request(cls):
        return cls._request
