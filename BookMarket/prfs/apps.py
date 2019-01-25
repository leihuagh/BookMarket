from django.apps import AppConfig
from django.db.models.signals import post_save


class PrfsConfig(AppConfig):
    name = 'prfs'

    def ready(self):
        from django.contrib.auth import get_user_model
        from .signals import profile_creator
        post_save.connect(profile_creator, sender=get_user_model())


