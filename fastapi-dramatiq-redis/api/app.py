from uuid import uuid4

from fastapi import FastAPI
from models import Job
from models import JobReceit
from models import JobRequest
from worker.app import job_example

app = FastAPI()


@app.post("/job")
def read_item(job_request: JobRequest) -> JobReceit:
    job_receit = JobReceit(task_id=uuid4())
    job_example.send(Job(request=job_request, receit=job_receit).json())
    return job_receit
