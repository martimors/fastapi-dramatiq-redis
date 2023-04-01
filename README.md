# FastAPI DramatiQ app example

This is intended as a practice example app using `FastAPI`, `DramatiQ` and `Redis` to create an
asynchronous API that has long running tasks.

## Run the app

```sh
# Start in docker
docker compose up

# Start a task
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"foo":"bar"}' \
  http://localhost:8080/job
```

## TODO

- ~~Dockerize~~
- Flesh out the example with polling endpoint and redirection + returning results
- Test that creates some tasks to test the app, maybe even `locust` just for fun
- In-memory (stub) broker for testing
- ~~Pre-commit hooks~~
- Other interesting parts of `DramatiQ`?
