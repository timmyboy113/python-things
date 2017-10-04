from socket import *
import thread
import util
import sys
 
def handler(clientsocket, clientaddr):
    print "Accepted clientsocketection from: ", clientaddr
    stored_data = ''
    while 1:
       # RECEIVE DATA
       data = clientsocket.recv(1024)

       # PROCESS DATA
       tokens = data.split(' ')            # Split by space at most once
       command = tokens[0]     	   # The first token is the command
       command = command.upper()
       if command=='GET':                    # The client requests the data
           clientsocket.send(stored_data)               # Return the stored data
       elif command=='STORE':                # The client want to store data
           stored_data = tokens[1]           # Get the data as second token, save it
           clientsocket.send('OK')                      # Acknowledge that we have stored the data
       elif command=='TRANSLATE':            # Client wants to translate
           stored_data = stored_data.upper() # Convert to upper case
           clientsocket.send(stored_data)              # Reply with the converted data
       elif command=='QUIT':                 # Client is done
           clientsocket.send('Quit')                 # Acknowledge
           break                             # Quit the loop
       elif command=='HELP':
           clientsocket.send('''
           Commands: \n
           Store = save a String \n
           Get = get saved String \n
           Translate = Strored String to upper \n
           Quit = Exit programm \n
           Dbversion = show mysql version \n
           register = benutzername,password,name,nachname,alter,geschlecht \n
           setupdb = creates database and tables \n
           getid = generate a random uniqe id \n
           userid = get user id (user *name des users*)
           ''')

       elif command=='DBVERSION':
           clientsocket.send(util.DBversion())
       elif command =='REGISTER':
           clientsocket.send(util.register(tokens[1], tokens[2], tokens[3], tokens[4], tokens[5], tokens[6]))
           
       elif command == 'GETID':
           clientsocket.send(util.getid())
  
       elif command == 'SETUPDB':
           clientsocket.send(util.setupdb())
 
       elif command == 'USERID':
           id = util.getuserid(tokens[1])
           clientsocket.send(id)

       else:
          clientsocket.send('Unknown command')

       # Close connection
    clientsocket.close()
    print "Client Disconnectet: ", clientaddr
 
if __name__ == "__main__":
 
    host = '0.0.0.0'
    port = 24069
    buf = 1024
 
    addr = (host, port)
 
    serversocket = socket(AF_INET, SOCK_STREAM)
 
    serversocket.bind(addr)
 
    serversocket.listen(2)
 
    while 1:
        print "Server is listening for clientsocketections\n"
 
        clientsocket, clientaddr = serversocket.accept()
        thread.start_new_thread(handler, (clientsocket, clientaddr))
    serversocket.close()
