#!/bin/bash
docker run -v ./src:/tmp --env-file ./env.redis  -it --name redisMaster testQueue.py;
