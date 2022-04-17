# UDP Server application

import socket

IP = "127.0.0.1"
PORT = 3001
buffer_size = 1024
MsgFromServer = "Hello from server"
bytesToSend = str.encode(MsgFromServer)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((IP, PORT))
print("UDP server up and listening")


while True:
    bytesAddressPair = UDPServerSocket.recvfrom(buffer_size)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)
    UDPServerSocket.sendto(bytesToSend, address)