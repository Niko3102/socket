import socket



SERVER_ADDRESS = '127.0.0.1'

SERVER_PORT = 22224

sock_listen = socket.socket()

sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))

sock_listen.listen(5)

print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))


while True:
    sock_service, addr_client = sock_listen.accept()
    print("\nConnessione ricevuta da " + str(addr_client))
    print("\nAspetto di ricevere i dati ")
    contConn=0
    while True:
        dati = sock_service.recv(2048)
        contConn+=1
        if not dati:
            print("Fine dati dal client. Reset")
            break
        
        dati = dati.decode()
        print("Ricevuto: '%s'" % dati)

        if dati=='0':
            print("Chiudo la connessione con " + str(addr_client))
            break
        else:
            separa = dati.split(";")
            if(separa[0] == "piu"):
                ris=float(separa[1])+float(separa[2])
            elif(separa[0] == "meno"):
                ris=float(separa[1])-float(separa[2])
            elif(separa[0] == "per"):
                ris=float(separa[1])*float(separa[2])
            elif(separa[0] == "diviso"):
                if(separa[2] != "0"):
                    ris=float(separa[1])/float(separa[2])     
                else:
                    ris ="Divisione per 0 impossibile"
        dati = "Risposta a : " + str(addr_client) + ". Il risultato di: " + separa[1] + " " + separa[0] + " " + separa[2] + " = " + str(ris)

        dati = dati.encode()

        sock_service.send(dati)

    sock_service.close()

