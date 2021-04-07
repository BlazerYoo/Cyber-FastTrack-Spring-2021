import socket

HOST = "cfta-nm01.allyourbases.co"
PORT = 8017

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	hex = s.recv(1024)
	ascii = hex.decode("unicode-escape")
	s.send(ascii.encode())
	s.send("\n".encode())
	flag = s.recv(1024)
	print(flag.decode())
