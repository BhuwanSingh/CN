import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('localhost', 3001)
sock.bind(server_address)

sock.listen(1)
print('Listening at {}'.format(server_address))

connection, client_address = sock.accept()
print('Accepted connection from {}'.format(client_address))

while True:
    command = input('Enter command: ')
    connection.send(command.encode())
    confirm = connection.recv(128).decode()
    if confirm == 'yes':
        print("Command sent")
    else:
        print("Command not sent")
        break