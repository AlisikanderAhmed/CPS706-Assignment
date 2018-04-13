#!/usr/bin/env python

import socket
import config
import time

UDP_IP = config.LOCAL_DNS_IP
UDP_PORT = config.LOCAL_DNS_PORT

#   Load Records Function
def loadrecords():
    records=[]
    records.append(["herCDN.com", "NSherCDN.com", "NS"])
    records.append(["NSherCDN.com", config.HER_CDN_IP, "A"])
    records.append(["video.hiscinema.com", "hiscinema.com", "CNAME"])
    records.append(["hiscinema.com", "NShiscinema.com", "NS"])
    records.append(["NShiscinema.com", config.HIS_CINEMA_IP, "A"])
    print records
    return records;

records = loadrecords();

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# Table of Records - Format (name, value, type)
try:
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print "received message:", data

        if data:
            print "Recieved data from this address: ", addr
            print "Resolving the DNS query"
            print "Query Resolved - Sending back to the client"
            record = config.HER_CDN_IP+':'+str(config.HER_CDN_PORT)
            query = record.encode()

            sock.sendto(query, addr)
except KeyboardInterrupt:
    print "\nForce Quit! GoodBye"
