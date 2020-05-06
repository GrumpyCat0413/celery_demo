import time
import random
from .celery_start import app


# name = 任务名字
@app.task()  # 任务注册
def send_msg(msg):
    print("msg={}".format(msg))
    time.sleep(2)
    print("sleep 2s  over")


@app.task()
def add(x, y):
    print("{}+{}={}".format(x, y, x + y))
    return x + y


"""
celery -A app.celery_proj worker -l info -P eventlet  -Q hello_async_tasks

nohup celery -A tasks.workers multi start 4 -P gevent -c 1000 --loglevel=INFO --logfile=/dockerdata/log/celery.log >/dev/null 2>&1 &
"""
