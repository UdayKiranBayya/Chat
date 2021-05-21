import socket
from configparser import ConfigParser
from threading import Thread
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

config_object = ConfigParser()
config_object.read("config.ini")
info = config_object["SERVERINFO"]
ip = info["clientip"]
port = int(info["clientport"])



s.connect((ip, port))
print("[+] Connected!")
class SendClient(Thread):
    def run(self):
        while True:
            msg = input ("Enter your message: ")
            msg = msg.encode()
            s.send(msg)
            print("[+] Message sent....")

class RecieveClient(Thread):
    def run(self):
        while True:
            receivedMsg = s.recv(1024)
            receivedMsg = receivedMsg.decode()
            print("Recieved:", receivedMsg)



        

SendClient().start()
RecieveClient().start()
     
    