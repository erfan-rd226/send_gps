import socket


ip = '127.0.0.1'
port =  52263

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((ip,port))
server_socket.listen(1)
