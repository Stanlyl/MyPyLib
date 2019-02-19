# coding=utf-8
from socket import*  

class TCP():
    def __init__(self, HOST, PORT, BUFF):
        self.ADDR = (HOST,PORT)
        self.BUFF = BUFF

    def transfer(self, message):
        if not message:
            return
        else:
            sk = socket(AF_INET, SOCK_STREAM)
            sk.connect(self.ADDR)
            sk.send(str(message).encode())
            data = sk.recv(self.BUFF).decode()
            sk.close()
            return data

class UDP():
    def __init__(self, HOST, PORT, BUFF):
        self.ADDR = (HOST,PORT)
        self.BUFF = BUFF

    def transfer(self, message):
        if not message:
            return
        else:
            sk = socket(AF_INET, SOCK_DGRAM)
            sk.sendto(str(message).encode(), self.ADDR)
            data = sk.recvfrom(self.BUFF)
            sk.close()
            return data

if __name__ == "__main__":
    HOST = gethostname()    # The remote host  
    PORT = 9686             # The same port as used by the server  
    client = UDP(HOST,PORT,1024)
    print(client.transfer('before ASNCoder...'))
