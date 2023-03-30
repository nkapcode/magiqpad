from core.serializers import BaseSerializer
from django.contrib.auth import get_user_model

class UserSerializer(BaseSerializer):
    """ User Serializer """

    class Meta:
        model = get_user_model()
        fields = '__all__'
