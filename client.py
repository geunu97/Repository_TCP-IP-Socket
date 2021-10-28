import socket

HOST = '175.205.118.55'  
PORT = 12351
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
data = raw_input('your data: ')
s. send(data)
reply = s.recv(1024)
print('Received Data from server : ' + reply)