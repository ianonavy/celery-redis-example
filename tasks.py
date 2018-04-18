import celery


celery_app = celery.Celery()
celery_app.conf.broker_url = 'redis://celery_redis:6379/0'
celery_app.conf.result_backend = 'redis://celery_redis:6379/1'


@celery_app.task
def add(a, b):
    print("Starting task 1")
    import time; time.sleep(5)
    print("Finished task 1")
    return a + b


@celery_app.task
def step2(total):
    import time; time.sleep(5)
    return -total
