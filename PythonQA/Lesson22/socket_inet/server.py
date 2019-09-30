"""
Запускаем в бекграунде
./server.py &
затем ps aux | grep <pid>
netstat -anp --tcp | grep server (смотрим tcp сокеты)
telnet localhost 9090


First of all we import socket which is necessary.
Then we made a socket object and reserved a port on our pc.
After that we binded our server to the specified port.
Passing an empty string means that the server can listen to incoming connections from other computers as well.
If we would have passed 127.0.0.1 then it would have listened to only those calls made within the local computer.
After that we put the server into listen mode.
5 here means that 5 connections are kept waiting if the server is busy and if a 6th socket trys to connect
 then the connection is refused.
At last we make a while loop and start to accept all incoming connections and change text to upper.
"""

import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(5)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()