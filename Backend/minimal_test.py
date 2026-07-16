import socket

print(socket.create_connection(("127.0.0.1", 3306), timeout=5))