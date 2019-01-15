# coding=utf-8
from socket import*  

HOST = 'localhost'    # The remote host  
PORT = 9686                 # The same port as used by the server  
s = None  

class TCP():
    def __init__(self, HOST, PORT, BECKUP):
        self.ADDR = (HOST,PORT)
        self.BECKUP = BECKUP

    def send(self, message):
        if not message:
            return
        else:
            self.sk = socket(AF_INET, SOCK_STREAM)
            self.sk.connect(self.ADDR)
            self.sk.send(message.encode('utf-8'))

    def recive(self):
            data = self.sk.recv(self.BECKUP).decode('utf-8')
            return data

    def close(self): 
            self.sk.close()  

    def client(self, message):
        while True:
            self.send(message)
            data = self.recive()
            if data == '$EndSection$':
                break
            else:
                print(data)
                self.sk.close()

if __name__ == "__main__":
    client = TCP(HOST,PORT,1024)
    client.client('hello')
