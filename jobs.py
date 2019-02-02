from apscheduler.schedulers.blocking import BlockingScheduler
from bot import create_tweet, teste

sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=1)
# def print_data():
# 	teste()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour='21-22', minute='0-59', timezone='America/Sao_Paulo')
def update_a():
 	create_tweet()


sched.start()