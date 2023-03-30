

import uuid
from django.db import models
from core.utils import get_now_date_time


class BaseModel(models.Model):
    """
    Base model for others to inherit from.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, help_text="Created on Datetime", editable=True)
    updated_at = models.DateTimeField(auto_now=True, help_text="Last Modified Datetime", editable=True)

    class Meta:
        """Additional options."""
        abstract = True
        ordering = ['-created_at']
    

    def __str__(self) -> str:
        return f"{self.id}"

class BaseModelIntPk(models.Model):
    """
    Base model for others to inherit from.
    """
    created_at = models.DateTimeField(auto_now_add=True, help_text="Created on Datetime", editable=True)
    updated_at = models.DateTimeField(auto_now=True, help_text="Last Modified Datetime", editable=True)

    class Meta:
        """Additional options."""
        abstract = True
    

    def __str__(self) -> str:
        return f"{self.id}"