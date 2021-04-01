#!/usr/bin/env python3

import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

sock_service = socket.socket()

sock_service.connect((SERVER_ADDRESS, SERVER_PORT))

print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))
protocollo=["SYN", "SYN ACK", "ACK with Data", "ACK for Data"]
step=0
while True:
    
    print("Invio: " + str(step) + " - " + protocollo[step])
    dati = str(protocollo[step])
    step+=1
    
    dati = dati.encode()

    sock_service.send(dati)

    dati = sock_service.recv(2048)

    if not dati:
        print("Server non risponde. Exit")
        break
    
    dati = dati.decode()
    print("Ricevuto: "+ str(step) + " - " + dati)

    if step == 3:
        print("Termino connessione")
        break
    step+=1
sock_service.close()