import time
import socket

print("Welcome to Chat Room")
print("Initiating connection...")
time.sleep(1)

s = socket.socket( family=socket.AF_INET, type=socket.SOCK_DGRAM )
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print("Server is up and running on ip: " + ip)
host = input("Enter the server's ip: ")
name = input("Enter your name: ")
port = 3001
print("Connecting to server...")
time.sleep(1)
serverAddress = (host, port)
print("Connected to: " + host)

s.sendto(name.encode(), serverAddress)
conn = s.recvfrom(1024)
s_name = conn[0].decode()
s_address = conn[1]
print("Connected to: " + s_name)

while True:
    message = s.recvfrom(1024)
    message = message[0].decode()
    print(s_name + ": " + message)
    message = input(name + ": ")
    if message == "quit":
        message = "Left the chat Room"
        s.sendto(message.encode(), s_address)
        print("\n")
        break
    s.sendto(message.encode(), s_address)
