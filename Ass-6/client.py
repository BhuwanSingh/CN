# UDP Client application

import socket

MsgFromClient = "Hello from client"
bytesToSend = str.encode(MsgFromClient)
server_address = ('localhost', 3001)
buffer_size = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(bytesToSend, server_address)

MsgFromServer = UDPClientSocket.recvfrom(buffer_size)
msg = MsgFromServer[0]
print(msg)