from core.models import BaseModelIntPk
from django.db import models

class Project(BaseModelIntPk):

    name = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL)
    body = models.JSONField(default=dict, null=True)
    characters = models.JSONField(default=dict, null=True)
    stories = models.JSONField(default=dict, null=True)

    class Meta:
        ordering = ['-id']


