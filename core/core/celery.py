import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

import django
django.setup()  # 💥 این خط مهمه!

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs):
    from tasks.tasks import remove_completed_tasks  # lazy import
    sender.add_periodic_task(
        crontab(minute='*/10'),
        remove_completed_tasks.s(),
        name="remove completed tasks every 10 minutes"
    )
