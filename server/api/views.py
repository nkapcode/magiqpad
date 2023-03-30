from api import serializers, models
from rest_framework import viewsets
from rest_framework.response import Response

class ProjectViewSet(viewsets.ModelViewSet):
    """ Project ViewSet """

    serializer_class = serializers.ProjectSerializer

    def get_queryset(self):
        """ Custom query set """
        return models.Project.objects.filter(user_id=self.request.user.id)

    def create(self, request):
        user_data = request.data.copy()
        user_data['user'] = request.user.id
        serializer = serializers.CreateProjectSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)
