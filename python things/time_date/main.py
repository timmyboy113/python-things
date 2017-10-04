import time

w = open("time.txt","wb")

while True:
     localtime = time.localtime(time.time()) 
     w.write( "Local current time : %s \n"% localtime)
     print("Zeit: %s" % localtime)
     time.sleep( 1 ) 