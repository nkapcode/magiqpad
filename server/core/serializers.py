from rest_framework import serializers
from django.conf import settings

class BaseSerializer(serializers.ModelSerializer):
    """ BaseSerializer Serializer """

    created_at = serializers.DateTimeField(input_formats=None, read_only=True)
    updated_at = serializers.DateTimeField(input_formats=None, read_only=True)