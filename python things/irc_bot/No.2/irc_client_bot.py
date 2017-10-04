# Import some necessary libraries.
import socket 

# Some basic variables used to configure the bot        
server = "hello.servebeer.com" # Server
channel = "#31" # Channel
botnick = "Bot" # Your bots nick


def ping(): # This is our first function! It will respond to server Pings.
  ircsock.send(bytes("PONG :pingis\n","utf-8)"))  

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  ircsock.send(bytes("PRIVMSG "+ chan +" :"+ msg +"\n","utf-8")) 

def joinchan(chan): # This function is used to join channels.
  ircsock.send(bytes("JOIN "+ chan +"\n","utf-8)"))

def hello(): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send(bytes("PRIVMSG "+ channel +" :Hello!\n","utf-8"))
  
def test():
  ircsock.send(bytes("PRIVMSG "+ channel +" :Der test hat funktionirt","utf-8"))
  
def help():
  ircsock.send(bytes("PRIVMSG "+ channel +" :Eine liste der aktuellen Befele: \n Help \n Hello + Botname \n test","utf-8"))
 
 
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick +" :This bot is a result of a tutoral covered on http://shellium.org/wiki.\n","utf-8")) # user authentication
ircsock.send(bytes("NICK "+ botnick +"\n","utf-8")) # here we actually assign the nick to the bot

joinchan(channel) # Join the channel using the functions we previously defined

#-----------------------------------------------------------------------------------------------------------------------

while 1: # Be careful with these! it might send you to an infinite loop
  ircmsg = ircsock.recv(2048) # receive data from the server
  ircmsg = ircmsg.strip(bytes('\n\r',"utf-8")) # removing any unnecessary linebreaks.
  print(ircmsg) # Here we print what's coming from the server

  if ircmsg.find(bytes(":Hello "+ botnick,"utf-8")) != -1: # If we can find "Hello Mybot" it will call the function hello()
    hello()

  if ircmsg.find(bytes("PING :","utf-8")) != -1: # if the server pings us then we've got to respond!
    ping()
  
  if ircmsg.find(bytes(":Help ","utf-8")) != -1: #  
    help()

  if ircmsg.find(bytes(":Test","utf-8")) != -1:
    test()
#----------------------------------------------------------------------------------------------------------------------
    
    
    
    
    