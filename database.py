#!/usr/bin/env python
# DataBase file which uses TCP to Establish connection

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 8000
BUFFER_SIZE = 1024  # Defulat size of 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((TCP_IP, TCP_PORT))
server.listen(1)

while True:
    conn, addr = server.accept()
    data = conn.recv(BUFFER_SIZE)
    print "Recieved data: ", data
    if data:
        file = open('database/video1.mp4', 'rb')
        packet = file.read(1024)
        while(packet):                  #While there is still content in the video
            conn.send(packet)           #Send that packet
            packet = file.read(1024)    #Read another packet
        file.close()
        conn.close()
