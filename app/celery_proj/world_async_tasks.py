import time
import random
from .celery_start import app


# name = 任务名字
@app.task()  # 任务注册
def world_send_msg(msg):
    print("world msg={}".format(msg))
    time.sleep(2)
    print("sleep 3s  over")


@app.task()
def world_add(x, y):
    print("{}+{}={}".format(x, y, x + y))
    return x + y
