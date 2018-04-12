from flask import Flask
from flask import render_template

import config   #Import Config file with our IP and Ports
import socket   #Import socket for UDP connection

app = Flask(__name__)

#Default routing URL to go to
@app.route("/")
def main():
    print config.HIS_CINEMA_IP
    print config.LOCAL_DNS_PORT
    return render_template('index.html')

@app.route("/load/")
def load():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    MESSAGE = "Testing!"

    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE

    #--------Establish UDP Connection with DNS--------
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

    #--------Client receives data back from DNS--------
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

    TCP_IP, TCP_PORT = str(data).split(':')

    BUFFER_SIZE = 1024
    MESSAGE = "Please respond with video file!"

    #--------Establish TCP Connection with Database--------
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
    s.connect((TCP_IP, int(TCP_PORT) ))
    s.send(MESSAGE)

    f = open('static/downloadedvideo1.mp4', 'wb')
    print "Error here"
    data = s.recv(BUFFER_SIZE)

    while(data):
        print "Receiving.."
        f.write(data)
        data = s.recv(BUFFER_SIZE)
    f.close()
    print "Download Complete!"
    s.close()

    return render_template('play.html', video = "/static/downloadedvideo1.mp4")


if __name__ == "__main__":
    app.run(host=config.HIS_CINEMA_IP, port=config.LOCAL_DNS_PORT, debug=False)
