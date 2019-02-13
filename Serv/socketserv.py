# coding=utf-8
import socketserver
import socket

class MyTCPHandler(socketserver.BaseRequestHandler): #服务类，监听绑定等等

    def handle(self):  #请求处理类，所有请求的交互都是在handle里执行的
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()#每一个请求都会实例化MyTCPHandler(socketserver.BaseRequestHandler):
        print("{} sent:".format(self.client_address[0]))
        print(self.data.decode())
        # just send back the same data, but upper-cased       
        self.request.send(self.data)

class MyUDPHandler(socketserver.BaseRequestHandler): #服务类，监听绑定等等

    def handle(self):  #请求处理类，所有请求的交互都是在handle里执行的
        # self.request is the UDP socket connected to the client
        self.data = self.request[0].strip()
        socket = self.request[1]
        print("{} sent:".format(self.client_address[0]))
        print(self.data.decode())
        # just send back the same data, but upper-cased       
        socket.sendto(self.data, self.client_address)

if __name__ == "__main__":
    HOST, PORT = socket.gethostbyname(socket.getfqdn(socket.gethostname())), 9686
    print(str(HOST)+':'+str(PORT)+' is on serve')
    # Create the server, binding to localhost on port 9999
    #server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    #server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)   #线程
    #server = socketserver.ThreadingUDPServer((HOST, PORT), MyUDPHandler)   #线程
    #server = socketserver.ForkingTCPServer((HOST, PORT), MyTCPHandler) #多进程TCP linux适用
    server = socketserver.ForkingUDPServer((HOST, PORT), MyUDPHandler) #多进程UDP linux适用
    # server = socketserver.TCPServer((HOST, PORT), MyTCPHandler) 单进程TCP
    # server = socketserver.UDPServer((HOST, PORT), MyUDPHandler) 单进程UDP
    
