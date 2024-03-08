from django.utils import timezone
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
