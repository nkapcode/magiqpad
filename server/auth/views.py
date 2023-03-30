from auth import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from auth.permissions import IsCreationOrIsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    """ User ViewSet """

    serializer_class = serializers.UserSerializer
    permission_classes = [IsCreationOrIsAuthenticated]

    def get_queryset(self):
        """ Custom query set """
        return get_user_model().objects.all()

    def create(self, request):
        user_data = request.data.copy()
        user_data['password'] = make_password(user_data['password'])
        serializer = self.get_serializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

    
    @action(detail=False, name='Get Logged In User', url_path='get-me', url_name='get_me')
    def get_me(self, request, *args, **kwargs):
        user = serializers.UserSerializer(request.user).data
        user['password'] = None
        return Response(user)

    



