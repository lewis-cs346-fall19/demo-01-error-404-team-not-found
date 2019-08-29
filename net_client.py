#!/usr/local/bin/python3

##############################
# alexander frenette
# frenette@email.arizona.edu
##############################

import socket

HOST = "localhost"
PORT = 4567

# set up the socket
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server, but does not return a new socket
SOCKET.connect((HOST, PORT))

print(str(SOCKET))

while True:
    try:
        # we need to send a message to the the server
        # get user input for a message to send
        usrInput = input()
    except EOFError as err:
        # We could probably more gracefully handle an EOF. In this implementation
        # you lose a line if you press EOF at the end of it.

        # the user pressed ctrl-d to signal end of file
        # close() will send an EOF to the peer connection
        SOCKET.close()
        exit()

    # send the user input to the server
    SOCKET.sendall(usrInput.encode())

    try:
        # with out new connection we will wait to recieve data, recv() return a
        # string
        recvStr = SOCKET.recv(4096).decode()
        print("Recieved String: " + recvStr)
    except ConnectionError as err:
        SOCKET.close()
        exit()
