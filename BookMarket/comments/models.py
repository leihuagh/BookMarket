from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Comments(models.Model):

    class Meta:
        verbose_name='комментарий',
        verbose_name_plural='комментарии'

    comments = models.TextField(
        'Comments',
        default=None
    )
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.comments
