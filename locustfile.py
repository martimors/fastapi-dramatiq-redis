from datetime import datetime
from random import randint
from random import seed

from locust import HttpUser
from locust import task

seed(datetime.now().timestamp())
upper = int(10e10)


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):  # noqa
        self.client.post(
            "/job",
            json={
                "first": randint(-upper, upper),  # nosec
                "second": randint(-upper, upper),  # nosec
            },
        )
