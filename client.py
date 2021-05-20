import socket
from threading import Thread
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '192.168.29.223'
port = 4569
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
     
    