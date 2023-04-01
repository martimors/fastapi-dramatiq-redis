#!/bin/sh
uvicorn api.app:app --host "0.0.0.0" --port "8080" & dramatiq worker.app
