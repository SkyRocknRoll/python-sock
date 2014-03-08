__author__ = 'uva'
import socket

sock = socket.socket()
data = raw_input()
try:
    sock.connect(('localhost', 9999), )
    sock.sendall(data + '\n')
    received = sock.recv(1024)
except Exception as e:
    print e

finally:
    sock.close()

print('Sent data {} '.format(data))
print('Received  data {} '.format(received))

