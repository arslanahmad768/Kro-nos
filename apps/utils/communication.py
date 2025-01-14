import json
import math
from base64 import b64decode, b64encode

from django.utils.translation import gettext_lazy as _

from rest_framework import serializers


def encode_dict_to_base64(data_dict):
    """Encode dict to base64 string."""
    encoded_data = b64encode(bytes(json.dumps(data_dict), 'utf-8')).decode('utf-8')
    return encoded_data


def decode_base64_to_dict(hash, error=ValueError):
    """Decode data from base64 string."""
    try:
        decoded_data_dict = json.loads(b64decode(hash))
    except Exception:
        raise error
    return decoded_data_dict


def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n
