import time
import socket

print("Welcome to Chat Room")
print("Initiating connection...")
time.sleep(1)

s = socket.socket( family=socket.AF_INET, type=socket.SOCK_DGRAM )
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 3001
s.bind((host, port))
print("Server is up and running on ip: " + ip + " port: " + str(port))
name = input("Enter your name: ")
conn = s.recvfrom(1024)
s_name = conn[0].decode()
s_address = conn[1]

print("Connected to: " + s_name)
s.sendto(name.encode(), s_address)

while True:
    message = input(name + ": ")
    if message == "quit":
        s.sendto(message.encode(), s_address)
        print("\n")
        break
    s.sendto(message.encode(), s_address)
    message = s.recvfrom(1024)
    message = message[0].decode()
    print(s_name + ": " + message)