from django.apps import AppConfig


class PhongConfig(AppConfig):
    name = 'phong'
    
    def ready(self):
            '''
            Any Scans that were incomplete in the last scan, we will mark them failed after
            server restarted
            This does not include pending_scans, pending_scans are taken care by celery
            '''
            pass