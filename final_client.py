from socket import *
from tkinter import *
from threading import *
host="localhost"
port=1420
buffer=1024
server=(host,port)
clientsock=socket(AF_INET,SOCK_STREAM)
clientsock.connect(server)
class ipbcc(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create()
        self.connect()
    def write(self,event):
        msg=self.e.get()
        clientsock.send(msg.encode())
    def create(self):

        self.pic=PhotoImage(file="logo.gif")
        self.label=Label(self,image=self.pic)
        self.label.grid(column=0)
        self.wall=Text(self,width=70,height=20,wrap=WORD)
        self.wall.grid(row = 0, column = 1, columnspan = 2, sticky = W)
        self.e=Entry(self,width=50)
        self.e.grid(row = 1, column = 1, sticky = W)
        self.e.bind('<Return>',self.write)
    def add(self,data):
        y=">>>"+data
        self.wall.insert(END,y)
    def connect(self):
        def xloop():
            while 1:
                data=clientsock.recv(buffer).decode()
                print(data)
                self.add(data)
        self.t = Thread(target=xloop, daemon=True)
        self.t.start()
                
root=Tk()
root.title("IPBCC v0.1")
app=ipbcc(root)
root.mainloop()
        
