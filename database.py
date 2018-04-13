#!/usr/bin/env python
# DataBase file which uses TCP to Establish connection

import socket
import config

TCP_IP = config.HER_CDN_IP
TCP_PORT = config.HER_CDN_PORT

BUFFER_SIZE = 1024  # Defulat size of 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((TCP_IP, TCP_PORT))
server.listen(5)

try:
    while 1:
        conn, addr = server.accept()
        data = conn.recv(BUFFER_SIZE)
        print "\nRecieved data: ", data
        if data:
            file = open('database/' +data+ '.mp4', 'rb')
            packet = file.read(BUFFER_SIZE)
            while(packet):                  #While there is still content in the video
                conn.send(packet)           #Send that packet
                packet = file.read(BUFFER_SIZE)    #Read another packet
            print data, "Transfer Complete!"
            file.close()
            conn.close()
except KeyboardInterrupt:
    print "\nForce Quit! GoodBye"
