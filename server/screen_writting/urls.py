"""screen_writting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import (views as ApiViews)
from auth import (views as AuthViews)

router = routers.DefaultRouter()
router.register(r'projects', ApiViews.ProjectViewSet, basename='projects')
router.register(r'users', AuthViews.UserViewSet, basename='users')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include('auth.urls')),
    path("api/v1/", include(router.urls)),
]



