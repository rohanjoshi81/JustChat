from socket import *
from tkinter import *
host=""
port=1420
buffer=1024
server=(host,port)
servsock=socket(AF_INET,SOCK_STREAM)
servsock.bind(server)
servsock.listen(1)
print('connecting ....')
while 1:
    tempsock,client=servsock.accept()
    print('connected')
    while 1:
        print('Recieving ... please wait ... listen to Muse ... ')
        data=tempsock.recv(buffer).decode()
        print(data)
        if not data:
            break
        data=input('Enter Data : ')
        tempsock.send(data.encode())
    tempsock.close()
serversock.close()
