import socket
import os
from time import sleep

def client():
    print('\nNew client ',  os.getpid())
    sleep(3)
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 8089))
    for i in range(50):
        print("Client %d sending %d" % (os.getpid(), i))
        clientsocket.send(('Hello ' + str(i) + '\n').encode())
        sleep(5)
    os._exit(0)


def server():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 8089))

    serversocket.listen(1)  # become a server socket, maximum 1 connection

    connection, address = serversocket.accept()

    while True:
        buf = connection.recv(64)
        if len(buf) > 0:
            print("Server received:", buf.decode())

newpid = os.fork()
if newpid == 0:
    client()
else:
    pids = (os.getpid(), newpid)
    print("parent: %d, child: %d\n" % pids)
    server()
