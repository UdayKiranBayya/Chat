import socket
from threading import Thread
from configparser import ConfigParser

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


config_object = ConfigParser()
config_object.read("config.ini")
info = config_object["SERVERINFO"]
ip = info["serverip"]
port = info["serverport"]
port = int(port)




maxClients = 1

s.bind((ip, port))
print("Server running at", ip, " ", port)
s.listen(maxClients)
conn, addr = s.accept()
print("[+] New connection!")

class Send(Thread):
    def run(self):
        while True:
            msg = input("Enter your message: ")
            msg = msg.encode()
            conn.send(msg)
            print("[+] Message sent....")
           
class Recieve(Thread):
    def run(self):
        while True:
            recievedMsg = conn.recv(1024)
            recievedMsg = recievedMsg.decode()
            print("Received:", recievedMsg)

Send().start() 
Recieve().start()     





