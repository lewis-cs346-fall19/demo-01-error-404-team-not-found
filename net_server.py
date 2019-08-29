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
SOCKET.bind((HOST, PORT))
SOCKET.listen()

while True:
    # accept is a blocking funtion
    conn, addr = SOCKET.accept()

    print("connection has been accepted: " + str(conn))

    while True:
        try:
            # with out new connection we will wait to recieve data
            recvStr = conn.recv(4096)
        except ConnectionError as err:
            # we want to still have the main socket continue to accept, but we will
            # close the socket for conn
            conn.close()
            # continue and start the while loop again and wait for a new inbound
            # connection
            break

        # the buffer will be empty if it is an EOF, which means that connection
        # has been closed. It is a tcp connection. There is a breakdown process.
        # recv() hides that from us, and will just return 0
        if len(recvStr) == 0:
            conn.close()
            print("Connection has been closed.")
            break

        # convert the recieved byte buffer to a string
        recvStr = recvStr.decode()

        # check the message we recieved
        print("Recieved String: " + recvStr)

        # now we modify the recieved string
        returnStr = recvStr.replace("Hello", "Goodbye")

        # check the modified message
        print("Return String: " + returnStr)

        # send back a message to the connection sendall() accepts a string
        conn.sendall(returnStr.encode())
