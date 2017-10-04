from os import *
from socket import *
from string import *
from random import *
from time import *
from thread import *




def connect(i):
  while True:
      print "LOOOOL"
      time.sleep(999999)

n = 0


while 1:
    try:
        start_new_thread(connect, (n,))
    except:
        print "FAIL"
