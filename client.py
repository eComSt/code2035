from threading import Thread
import socket

s = socket.socket()
s.connect(('51.250.65.169', 5002))
print(f"[+] connected")
name = input("Enter your name: ")

def listen_s():
    while True:
        try:
            data = s.recv(1024).decode()
            print("\n"+data)
        except:pass
t = Thread(target=listen_s)
t.daemon = True
t.start()

while True:
    to_send = input("")
    if to_send == "exit":
        break
    to_send = name + ": " + to_send
    s.send(to_send.encode())

s.close()