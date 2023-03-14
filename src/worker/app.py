from time import sleep

import dramatiq
from dramatiq.brokers.redis import RedisBroker
from models import JobRequest


redis_broker = RedisBroker(host="localhost")
dramatiq.set_broker(redis_broker)


@dramatiq.actor
def job_example(job: JobRequest) -> None:
    print("Job is running!")
    print(job.json())
    sleep(10)
    print("Job finished!")
