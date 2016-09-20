#!/bin/sh
/usr/bin/redis-server --daemonize yes --protected-mode no
/usr/local/bin/python /tmp/testQueue.py
