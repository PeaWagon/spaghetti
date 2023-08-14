from django.db import models
from django.contrib.auth.models import User

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # this must match the data type for the primary key of the related object
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
