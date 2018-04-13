from flask import Flask
from flask import render_template

import config   #Import Config file with our IP and Ports
import socket   #Import socket for UDP connection

#from signal import signal, SIGPIPE, SIG_DFL    #For Error Handling with UDP Conncetion
#signal(SIGPIPE,SIG_DFL) #For Error Handling with UDP Conncetion

BUFFER_SIZE = 1024

app = Flask(__name__)

#Default routing URL to go to
@app.route("/")
def main():
    return render_template('index.html')

#--------Establish UDP Connection with DNS--------
def DNS_Message(MESSAGE):
    UDP_IP = config.LOCAL_DNS_IP
    UDP_PORT = config.LOCAL_DNS_PORT

    print "\nUDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE, "\n"

    UDP_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    UDP_Socket.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    data, addr = UDP_Socket.recvfrom(BUFFER_SIZE)
    TCP_IP, TCP_PORT = str(data).split(':')

    print "Please respond with video file!"

    return TCP_IP, TCP_PORT

#--------Establish TCP Connection with Database--------
def file_Downlaod(addr, port, filename):
    TCP_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP Connection
    TCP_Socket.connect((addr, int(port) ))
    TCP_Socket.send(filename)

    file = open('static/downloaded'+filename+'.mp4', 'wb')  #Open File
    data = TCP_Socket.recv(BUFFER_SIZE)                     #Get Data

    while(data):
        print "Receiving " + filename + " contents now.."
        file.write(data)                        #Write Files Data
        data = TCP_Socket.recv(BUFFER_SIZE)     #Get More data

    file.close()            #Close File Connection
    print "Download Complete!"
    TCP_Socket.close()      #Close TCP Connection


#--------Path for file 1--------
@app.route("/F1/")
def F1():
    TCP_IP, TCP_PORT = DNS_Message('hiscinema.com/File1')
    file_Downlaod(TCP_IP, TCP_PORT, 'video1')
    return render_template('play.html', video = "/static/downloadedvideo1.mp4")
#--------Path for file 2--------
@app.route("/F2/")
def F2():
    TCP_IP, TCP_PORT = DNS_Message('hiscinema.com/File2')
    file_Downlaod(TCP_IP, TCP_PORT, 'video2')
    return render_template('play.html', video = "/static/downloadedvideo2.mp4")
#--------Path for file 1--------
@app.route("/F3/")
def F3():
    TCP_IP, TCP_PORT = DNS_Message('hiscinema.com/File3')
    file_Downlaod(TCP_IP, TCP_PORT, 'video3')
    return render_template('play.html', video = "/static/downloadedvideo3.mp4")
#--------Path for file 1--------
@app.route("/F4/")
def F4():
    TCP_IP, TCP_PORT = DNS_Message('hiscinema.com/File4')
    file_Downlaod(TCP_IP, TCP_PORT, 'video4')
    return render_template('play.html', video = "/static/downloadedvideo4.mp4")


#Main, App.run()
if __name__ == "__main__":
    app.run(host=config.HIS_CINEMA_IP, port=config.HIS_CINEMA_PORT, debug=False)
