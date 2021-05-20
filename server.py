import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "127.0.0.1"
port = 4567
maxClients = 1

s.bind((ip, port))
s.listen(maxClients)
conn, addr = s.accept()
print("[+] New connection with", addr, "sucessfully!")

while True:
    msg = input("Enter your message: ")
    if msg != 'end':
        msg = msg.encode()
        conn.send(msg)
        recievedMsg = conn.recv(1024)
        recievedMsg = recievedMsg.decode()
        print(recievedMsg)
    else:
        msg = msg.encode()
        conn.send(msg)
        #os.system("npx kill-port 4567")
        print("Terminating  your program: ")
        break
