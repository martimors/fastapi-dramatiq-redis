# FastAPI DramatiQ app example

This is intended as a practice example app using `FastAPI`, `DramatiQ` and `Redis` to create an asynchronous API that has long running tasks.

## Run the app

```
# Start redis
docker compose up -d

# Install dependencies
poetry install

# Start worker and API
poetry shell
uvicorn src.api.app:app & dramatiq src.worker.app
```

## TODO

- Dockerize
- Flesh out the example with polling endpoint and redirection + returning results (`Result` middleware)
- Test that creates some tasks to test the app, maybe even `locust` just for fun
- Pre-commit hooks
- Other interesting parts of `DramatiQ`?
