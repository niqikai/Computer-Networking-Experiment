# 简单Web服务器，它仅能处理一个请求。
# 1 当一个客户端连接时创建一个套接字
# 2 从这个连接接收HTTP请求
# 3 解释该请求已确定所请求的特定文件
# 4 从服务器文件系统获得请求的文件
# 5 创建一个由请求的文件组成的HTTP响应报文，报文前有首部行
# 6 经过TCP连接请求的浏览器发送响应，如果请求的文件不存在返回"404 Not Found"差错报文

from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind('', 6789)
serverSocket.listen(1)

while True:
    print('ready to server ...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outPutData = f.read()

        header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outPutData))
        connectionSocket.send(header.encode())

    except IOError:
        header = 'HTTP/1.1 404 Not Found'
        connectionSocket.send(header.encode())

        connectionSocket.close()

        serverSocket.close()

