from django.apps import AppConfig


class ScoringAppConfig(AppConfig):
    name = 'scoring_app'

    def ready(self):
        import scoring_app.signals
