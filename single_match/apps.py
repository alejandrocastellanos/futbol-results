from django.apps import AppConfig


class SingleMatchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'single_match'

    def ready(self):
        import single_match.signals
