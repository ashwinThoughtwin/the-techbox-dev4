from celery import Celery


    

app.conf.beat_schedule = {
    "run-in-10-seconds-task": {
        "task": "tasks.send_mail",
        "schedule": 10.0
    }
}