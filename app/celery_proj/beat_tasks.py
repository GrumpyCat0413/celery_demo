from .celery_start import app


@app.task()
def hello(x, y):
    print("hello world")


@app.task()
def world(x, y):
    print("hello world")
