from http import HTTPStatus

from fastapi import FastAPI
from models import JobRequest
from worker.app import job_example

app = FastAPI()


@app.post("/job")
def read_item(job: JobRequest) -> int:
    job_example.send(job)
    return HTTPStatus.ACCEPTED
