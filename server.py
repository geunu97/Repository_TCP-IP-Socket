import socket
import sys                
import RPi.GPIO as GPIO  

GPIO.setmode(GPIO.BOARD)  
LED = 11                  
GPIO.setup(LED,GPIO.OUT, initial=GPIO.LOW)

HOST = '175.205.118.55'
PORT = 12351
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print('Socket created')

try:
s.bind((HOST, PORT))
s.listen(socket.SOMAXCONN)
except socket.error:
print('Bind failed')

s.listen(5)
print('Socket awaiting messages')
(conn, addr) = s.accept()
print('Connected')

while True:
data = conn.recv(1024)

if data == 'Close':
break
else:
if data == 'LED ON':    
print("LED_ON")                      
       GPIO.output(LED, GPIO.HIGH)              
if data == 'LED OFF':                            
       print("LED_OFF")                    
       GPIO.output(LED, GPIO.LOW)              

print('Received data from client : ' + data)
reply = data
conn. send(reply)
conn.close()