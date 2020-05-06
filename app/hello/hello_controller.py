from datetime import datetime
from . import api
from app.celery_proj.hello_async_tasks import send_msg, add
from app.celery_proj.world_async_tasks import world_send_msg


# from ..celery_proj.hello_async_tasks import send_msg, add
# 绝对路径引入

@api.route('/')
def hello_world():
    cur_time = str(datetime.now())
    send_msg.delay("this is test task ={0}".format(cur_time))
    # send_msg.apply_async(args=["this is test task ={0}".format(cur_time)], queue='hello_async_queue')
    # send_msg.apply_async(args=["this is test task ={0}".format(cur_time)])
    return 'Hello World! {0}'.format(cur_time)


@api.route('/add')
def hello_add():
    rel = add.delay(1, 2)
    return 'hello_add {0}'.format(rel)


@api.route('/1')
def world_world():
    cur_time = str(datetime.now())
    # send_msg.delay("this is test task ={0}".format(cur_time))
    # world_send_msg.apply_async(args=["this is test task ={0}".format(cur_time)], queue='world_async_queue')
    # world_send_msg.apply_async(args=["this is test task ={0}".format(cur_time)])
    return 'Hello World! {0}'.format(cur_time)
