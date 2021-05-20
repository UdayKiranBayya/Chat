import socket
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "192.168.29.223"
port = 4569
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





