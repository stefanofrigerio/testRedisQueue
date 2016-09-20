#!/bin/bash
echo "***** start redis queue spike ******\n"
if [ -z "$1" ]
  then
    echo "you must provide the number of the consumers e.g. [./start.redis.queue.sh 1]"
    exit 0
fi
cwd=$(pwd)
echo "***** build the containers ******\n"
docker rm -f redisProducer
docker rm -f postgres
docker build -t producer -f Dockerfile.producer . 
docker build -t consumer -f Dockerfile.consumer . 
docker build -t persistence -f Dockerfile.postgres .
echo "***** start the postgres *****"
docker run --name postgres -e POSTGRES_PASSWORD=mysecretpassword -d persistence
echo "***** now start the producer ******\n"
docker run -v ${cwd}/src:/tmp --env-file ./env.redis --name redisProducer -d producer
