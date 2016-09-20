#!/bin/sh
/usr/bin/redis-server --daemonize yes
/usr/local/bin/python /tmp/testQueue.py
