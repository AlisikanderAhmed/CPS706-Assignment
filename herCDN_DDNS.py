#!/usr/bin/env python
#<------herCDN DDNS File, Uses UDP to connect with Local DNS to resolve local DNS queries------>

import socket
import config
import time
import sqlite3

UDP_IP = "0.0.0.0"
UDP_PORT = 44494

#   Load Records Function and insert into Database
def initRecords():
    connection = sqlite3.connect('HERCDN_Records.db')
    c = connection.cursor()

    c.execute('DROP TABLE IF EXISTS HERCDN_Records')
    c.execute('''CREATE TABLE HERCDN_Records (Name text, Value text, Type text)''')

    records=[('herCDN.com', 'NSherCDN.com', 'NS'), ('NSherCDN', 'localhost', 'A'),
            ('hiscinema.com', 'NShiscinema.com', 'NS'), ('NShiscinema.com', 'localhost', 'A'),
            ('herCDN.com', 'localhost', 'A')]

    c.executemany('INSERT INTO HERCDN_Records VALUES (?,?,?)', records)

    connection.commit()
    connection.close()

#   Query Database to find the record client is looking for
def DNS_Query(record):
    connection = sqlite3.connect('HERCDN_Records.db')
    conn = connection.cursor()

    name = record.split(',')[0]
    type = record.split(',')[1]

    connection.close()
    return answer

initRecords()

#--------Establish UDP Connection with Client--------
UDP_Socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
UDP_Socket.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = UDP_Socket.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data

    if data:
        print "Recieved data from this address: ", addr
        print "Let me resolve the DNS query"
        print "It is done - sending back to the client"

        UDP_Socket.sendto(DNS_Query(data), addr)
