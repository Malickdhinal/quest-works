import socket
s=socket.socket()
s.connect(("localhost",9999))
name=input("enter name:")
s.send(name.encode())
print(s.recv(100).decode()) 