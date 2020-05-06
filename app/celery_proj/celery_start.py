# from __future__ import absolute_import
from celery import Celery

# app = Celery('proj',
#              broker='redis://localhost:6379/0',
#              backend='redis://localhost:6379/0',
#              include=['app.celery_proj.hello_async_tasks',
#                       'app.celery_proj.world_async_tasks']
#              )
# include=['celery_proj.tasks']
# include :任务路径
"""
include:路径 一定要写对，与 后台执行celery有关
celery -A celery_proj worker -l info -P eventlet  -Q hello_async_tasks

# 其实 可以指定celery app 实例 如下,（默认找的是celery文件名，这里面我们换成 celery_start.py文件）
# celery -A celery_proj.celery_start worker -l info -P eventlet  -Q hello_async_tasks
# celery -A app.celery_proj.celery_start worker -l info -P eventlet  -Q hello_async_queue

如果 include 的任务路径填写为
app.celery_proj.hello_async_tasks

则可以在 app文件夹同级目录下 可执行启动相应的 celery
cmd : celery -A app.celery_proj worker -l info -P eventlet  -Q hello_async_tasks
[tasks]
  . app.celery_proj.hello_async_tasks.add
  . app.celery_proj.hello_async_tasks.send_msg
"""
# app.conf.update(result_expires=300)


app = Celery("celery_proj")
app.config_from_object('app.celery_proj.config')


if __name__ == '__main__':
    app.start()
