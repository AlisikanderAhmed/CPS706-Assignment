#!/usr/bin/env python

import socket
import config
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

HerDNS_IP = "141.117.232.29"
HisDNS_IP = "141.117.232.30"

#   Load Records Function
def loadrecords():
    records=[]
    records.append(["herCDN.com", "NSherCDN.com", "NS"])
    records.append(["NSherCDN.com", HerDNS_IP, "A"])
    records.append(["video.hiscinema.com", "hiscinema.com", "CNAME"])
    records.append(["hiscinema.com", "NShiscinema.com", "NS"])
    records.append(["NShiscinema.com", HisDNS_IP, "A"])
    print records
    return records;

records = loadrecords();

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# Table of Records - Format (name, value, type)

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data

    if data:
        print "Recieved data from this address: ", addr
        print "Let me resolve the DNS query"
        print "It is done the 127.0.0.1:8000 - give back to the client"

        sock.sendto(b'127.0.0.1:8000', addr)
