import socket

print(socket.getaddrinfo("ya.ru", 80))
ip = socket.gethostbyname('www.google.com')
print(ip)
