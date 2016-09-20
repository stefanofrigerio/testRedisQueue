# testRedisQueue spike
## what is and how it works
* a simple producer who send a random varchar(64) string as a key on a redis queue
* n consumer that pop that queue and write the value on a shared postgres instance
* simply execute ./start.redis.queue.spike.sh
