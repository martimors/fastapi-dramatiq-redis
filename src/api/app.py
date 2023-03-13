from fastapi import FastAPI
from models import JobRequest
from http import HTTPStatus

from worker.app import job_example

app = FastAPI()


@app.post("/job")
def read_item(job: JobRequest):
    job_example.send()
    return HTTPStatus.ACCEPTED
