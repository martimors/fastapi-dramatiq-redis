import dramatiq
from models import JobResult

from dramatiq.brokers.redis import RedisBroker
from time import sleep


redis_broker = RedisBroker(host="localhost")
dramatiq.set_broker(redis_broker)


@dramatiq.actor
def job_example() -> JobResult:
    print("Job is running!")
    sleep(10)
    print("Job finished!")
