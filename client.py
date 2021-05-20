import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 4567
s.connect((ip, port))
print("[+] Connected..")

while True:
    receivedMsg = s.recv(1024)
    receivedMsg = receivedMsg.decode()
    if receivedMsg != "end":
        print(receivedMsg)
        msg = input ("Enter your message: ")
        msg = msg.encode()
        s.send(msg)
    else:
        #os.system("npx kill-port 4567")
        print("Terminating your program")
        break

    