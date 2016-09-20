#!/bin/bash
echo "***** start redis queue spike ******"
if [ -z "$1" ]
  then
    echo "you must provide the number of the consumers e.g. [./start.redis.queue.sh 1]"
    exit 0
fi
cwd=$(pwd)
echo "***** build the containers ******\n"
docker rm -f redisProducer
docker rm -f postgres
docker rm -f $(docker ps -a -f name=redisConsumer* -q)
docker build -t producer -f Dockerfile.producer . 
docker build -t consumer -f Dockerfile.consumer . 
docker build -t persistence -f Dockerfile.postgres .
echo "***** start the postgres *****"
docker run --name postgres -e POSTGRES_PASSWORD=mysecretpassword -d persistence
sleep 2
echo "***** now start the producer ******"
docker run -v ${cwd}/src:/tmp --env-file ./env.redis --name redisProducer -d producer
sleep 2
echo "***** now start the $1 consumers ******"
for ((i=1; i<=$1; i++)); do
	echo "start consumer $i"
	docker run -v ${cwd}/src:/tmp --env-file ./env.redis --link postgres:persistence --link redisProducer:producer --name redisConsumer$i -d consumer
done
echo "***** DONE *****"
echo "now attach each N consumers in a N different terminals using \"docker attach redisConsumer<N>\""
echo "To terminate and see the output \"docker kill postgres\". Any error should kill the consumer."
