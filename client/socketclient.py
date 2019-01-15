# coding=utf-8
from socket import*  

HOST = 'localhost'    # The remote host  
PORT = 9686                 # The same port as used by the server  
s = None  

class TCP():
    def __init__(self, HOST, PORT, BUFF):
        self.ADDR = (HOST,PORT)
        self.BUFF = BUFF
        self.sk = socket(AF_INET, SOCK_STREAM)
        self.sk.connect(self.ADDR)

    def send(self, message):
        if not message:
            return
        else:
            self.sk.send(message.encode())
            self.sk.close()

    def shutdown():
        pass

if __name__ == "__main__":
    client = TCP(HOST,PORT,1024)
    client.send('fuck')
