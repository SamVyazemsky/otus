import socket
import ssl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
addr = ('www.google.com', 443)
ss.connect(addr)
ss.send(b'GET / HTTP/1.0\r\n\r\n')
resp = ss.recv(1000)
print(resp)
ss.close()
