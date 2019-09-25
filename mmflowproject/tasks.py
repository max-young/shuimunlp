from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost:5462//')


@app.task
def add(x, y):
    return x + y
