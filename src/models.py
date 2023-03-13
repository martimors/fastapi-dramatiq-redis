from pydantic import BaseModel


class JobRequest(BaseModel):
    foo: str


class JobResult(BaseModel):
    bar: str
