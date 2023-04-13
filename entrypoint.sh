#!/bin/sh
MODE=$1

if [ $MODE = "worker" ]; then
    dramatiq worker.app
elif [ $MODE = "api" ]; then
    uvicorn api.app:app --host "0.0.0.0" --port "8080"
elif [ $MODE = "combined" ]; then
    uvicorn api.app:app --host "0.0.0.0" --port "8080" & dramatiq worker.app
else
    echo "mode $MODE not valid, must be worker, api or combined"
    exit 1
fi
