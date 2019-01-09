from socket import*  

HOST = 'xxx.xxx.xxx.xxx'    # The remote host  
PORT = 9686                 # The same port as used by the server  
s = None  

def startClient():
    BUFSIZE = 1024  
    ADDR = (HOST, PORT)  


    while True:  
        data = input('> ')  
        if not data:  
            break  
        tcpCliSock = socket(AF_INET, SOCK_STREAM)  
        tcpCliSock.connect(ADDR)  
        tcpCliSock.send(data.encode())  
        data = tcpCliSock.recv(BUFSIZE).decode()  
        print(data)  
        tcpCliSock.close()  

if __name__ == "__main__":
    root = startClient()
    root.mainloop()
