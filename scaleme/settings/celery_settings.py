import os
# from kombu import Queue

# from .base import TIME_ZONE as DJANGO_TIME_ZONE

BROKER_URL = os.environ.get("BROKER_URL", "redis://localhost:6379/0")

CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", 'redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# CELERY_TIMEZONE = DJANGO_TIME_ZONE
# CELERY_ENABLE_UTC = True

# CELERY_DEFAULT_QUEUE = 'tasks'
# CELERY_QUEUES = (
#     Queue('tasks', routing_key='task.#'),
#     Queue('transient', routing_key='transient.#', delivery_mode=1)
# )
# CELERY_DEFAULT_EXCHANGE = 'tasks'
# CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
# CELERY_DEFAULT_ROUTING_KEY = 'task.default'


# """
#     Needed to add:
#     1. Retries.
#     2. Email to admin if something failed.
#     3. Arrange the app configration for a sepreate application,
#        so its easy to create seperate celery application and to configure.
#     4. "http://docs.celeryproject.org/en/latest/userguide/routing.html",
#     5. "http://docs.celeryproject.org/en/latest/userguide/monitoring.html",
#     6. Using monitors.
# """
