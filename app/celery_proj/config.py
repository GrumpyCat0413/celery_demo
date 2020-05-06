from __future__ import absolute_import
from celery.schedules import crontab
from datetime import timedelta

broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/0'
task_serializer = 'json'
result_serializer = 'json'
timezone = 'Asia/Shanghai'
enable_utc = False
accept_content = ['json']
result_accept_content = ['json']
result_expires = 100
# imports = ('app.celery_proj.hello_async_tasks',
#            'app.celery_proj.world_async_tasks')

include = ['app.celery_proj.hello_async_tasks',
           'app.celery_proj.world_async_tasks',
           'app.celery_proj.beat_tasks']

task_routes = {
    'app.celery_proj.hello_async_tasks.*': {
        'queue': 'hello_async_queue',
    },
    # 'app.celery_proj.hello_async_tasks.add': {
    #     'queue': 'hello_async_queue'
    # },
    'app.celery_proj.world_async_tasks.add': {
        'queue': 'hello_async_queue'
    },
    'app.celery_proj.world_async_tasks.world_send_msg': {
        'queue': 'my_async_queue'
    },
    'app.celery_proj.beat_tasks.*': {
        'queue': 'beat_task_queue'
    },
}
# 如果 函数调用的地方，给定queue的参数，那么将会覆盖配置文件中的对应的queue

# 设置定时任务:
beat_schedule = {
    'hello_task': {
        'task': 'app.celery_proj.beat_task.hello',
        'schedule': timedelta(seconds=10),
        'args': (2, 8)
    },
    'world_task': {
        'task': 'app.celery_proj.beat_task.world',
        'schedule': crontab(minute="*/1"),
        'args': (4, 5)
    }
}

# 定时任务beat 启动规则：
# 1、首先应该启动 发布任务，将所有的定时任务发送到指定的queue中，如果不启动消费者的话，将会一直发送，造成积压
# 指定定时任务的task_routes 的相关定时任务的queue 则将定时任务发往对应的queue中，需要指定消费者消费指定的queue
# celery -A app.celery_proj.celery_start beat -l info

# 2、启动消费者 进行消费定时任务，有多少积压 就同时消费多少个任务
# celery -A app.celery_proj.celery_start worker -l info -P eventlet

# task_routes 中 不指定 定时任务的 队列 默认是 celery中，指定后，可以指定消费queue来执行定时任务
# celery -A app.celery_proj.celery_start worker -l info -P eventlet -Q beat_task_queue

# 当然最好发布任务与消费 应该一起启动
# celery -A app.celery_proj.celery_start worker -l info -P eventlet -Q beat_task_queue

# 另外注意：在windows下 不能够使用一条语句 命令 执行 发布任务和消费任务
# celery -B -A app.celery_proj.celery_start worker -l info -P eventlet -Q beat_task_queue