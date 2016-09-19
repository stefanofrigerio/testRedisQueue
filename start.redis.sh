#!/bin/sh
/usr/bin/redis-server --daemonize yes
/usr/local/bin/python /tmp/$1
