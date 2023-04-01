from pydantic import BaseModel
from pydantic import UUID4


class JobRequest(BaseModel):
    foo: str


class JobReceit(BaseModel):
    task_id: UUID4


class Job(BaseModel):
    request: JobRequest
    receit: JobReceit
