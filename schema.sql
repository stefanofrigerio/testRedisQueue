create user redis with password 'redis';
create database redis owner redis;
\c redis
create table queue (key varchar(100), value varchar(200), constraint key primary key(key));
grant all privileges on queue to redis;
