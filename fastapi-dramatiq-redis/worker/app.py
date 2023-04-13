import dramatiq
from dramatiq.brokers.redis import RedisBroker
from models import Job
from settings import settings

redis_broker = RedisBroker(url=settings.REDIS_DSN)
dramatiq.set_broker(redis_broker)


@dramatiq.actor()
def job_example(job_str: str) -> None:
    job: Job = Job.parse_raw(job_str)
    print(
        f"RESULT {job.receit.task_id}: "
        f"{job.request.first}+{job.request.second}"
        f"={job.request.first+job.request.second}"
    )
