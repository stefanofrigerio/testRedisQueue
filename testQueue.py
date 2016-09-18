'''
Created on Sep 16, 2016

@author: stefanofrigerio
'''
import redis
import string
import random
import sys
import time


r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.flushdb()

def id_generator(size=64, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class Queue(object):
    """An abstract FIFO queue"""
    def __init__(self):
        local_id = r.incr("queue_space")
        id_name = "test"
        self.id_name = id_name

def push(self, element):
        id_name = self.id_name
        push_element = r.lpush(id_name, element)

def pop(self):
        id_name = self.id_name
        popped_element = r.rpop(id_name)
        return popped_element
    
q = Queue()
i=0
tstart = time.time()
try:
    while(1):
        push(q,id_generator())
        i=i+1
except (KeyboardInterrupt, SystemExit):
    pass
finally:
    tend = time.time()
    print "***** inserted ["+str(i)+"] values in "+str(tend-tstart)+" seconds, "+str(i/(tend-tstart))+" per second"