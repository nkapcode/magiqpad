from core.serializers import BaseSerializer
from api import models
from auth.serializers import UserSerializer 

class ProjectSerializer(BaseSerializer):
    """ Project with read only user object Serializer """

    user = UserSerializer(read_only=True)

    class Meta:
        model = models.Project
        fields = '__all__'

class CreateProjectSerializer(BaseSerializer):
    """ Project Serializer """
    class Meta:
        model = models.Project
        fields = '__all__'
    