import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_k8s_starter.settings')

app = Celery('django_k8s_starter')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
def demo_task():
    print('The demo works!')
