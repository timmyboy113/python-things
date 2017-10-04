import socket

HOST = '127.0.0.1'   # Symbolic name meaning the local host
PORT = 24069    # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    command = raw_input('Enter your command: ')
    if command.split(' ')[0]=='STORE':
        while True:
            additional_text = raw_input()
            command = command+'\n'+additional_text
            if additional_text=='.':
                break
    s.send(command)
    reply = s.recv(1024)
    if reply=='Quit':
        break
    print reply
