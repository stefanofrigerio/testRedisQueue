import redis
import string
import random

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
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

while(1):
    push(q,id_generator())


