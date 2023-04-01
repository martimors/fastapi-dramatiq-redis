from random import randint
from time import sleep

import dramatiq
from dramatiq.brokers.redis import RedisBroker
from models import Job
from settings import settings

redis_broker = RedisBroker(url=settings.REDIS_DSN)
dramatiq.set_broker(redis_broker)


@dramatiq.actor()
def job_example(job_str: str) -> None:
    job: Job = Job.parse_raw(job_str)
    print(f"Job {job.receit.task_id} is running!")
    sleep(randint(1, 10))  # nosec
    print(f"Job {job.receit.task_id} finished!")
