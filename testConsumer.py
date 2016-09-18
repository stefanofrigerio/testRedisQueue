import redis
import string
import random
import psycopg2
import sys
import time

r = redis.StrictRedis(host='localhost', port=6379, db=0)
conn_string = "host='localhost' dbname='spark' user='spark' password='spark'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

def id_generator(size=64, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class Queue(object):
    """An abstract FIFO queue"""
    def __init__(self):
        local_id = r.incr("queue_space")
        #id_name = "queue:%s" %(local_id)
        id_name = "test"
        self.id_name = id_name

def push(self, element):
        id_name = self.id_name
        push_element = r.lpush(id_name, element)

def pop(self):
        #id_name = self.id_name
        popped_element = r.blpop("test")
        #popped_element = r.rpop("test")
        #print popped_element
        #return popped_element
        print str(popped_element).split(',')[1].replace("'","").replace(")","")
        return str(popped_element).split(',')[1].replace("'","").replace(")","")
    
q = Queue()
i=0
tstart = time.time()
try:
    while(1):
        cursor.execute("insert into queue values ('"+pop('test')+"','testvalue');")
        i=i+1
        conn.commit()
except (KeyboardInterrupt, SystemExit):
    pass
finally:
    tend = time.time()
    print "***** consumed ["+str(i)+"] items in "+str(tend-tstart)+" seconds, "+str(i/(tend-tstart))+" per second"
    
