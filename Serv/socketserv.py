# coding=utf-8
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler): #服务类，监听绑定等等
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
 
    def handle(self):  #请求处理类，所有请求的交互都是在handle里执行的
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()#每一个请求都会实例化MyTCPHandler(socketserver.BaseRequestHandler):
        print("{} wrote:".format(self.client_address[0]))
        print(self.data.decode())
        # just send back the same data, but upper-cased       
        self.request.send(self.data)#sendall是重复调用send.

if __name__ == "__main__":
    HOST, PORT = 'localhost', 9686

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    #server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)   #线程
    server  = socketserver.ForkingTCPServer((HOST, PORT), MyTCPHandler) #多进程 linux适用
# server = socketserver.TCPServer((HOST, PORT), MyTCPHandler) 单进程