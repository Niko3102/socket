import socket
from threading import Thread

SERVER_ADDRESS = '127.0.0.1'

SERVER_PORT = 22224


def ricevi_comandi(sock_service, addr_client):
    print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))


    while True:
        print("\nConnessione ricevuta da " + str(addr_client))
        print("\nAspetto di ricevere i dati ")
        while True:
            dati = sock_service.recv(2048)
            if not dati:
                print("Fine dati dal client. Reset")
                break
            
            dati = dati.decode()
            print("Ricevuto: '%s'" % dati)

            if dati=='0':
                print("Chiudo la connessione con " + str(addr_client))
                break
            else:
                separa = dati.split(";")#separa i dati ricevuti tramite il punto e virgola (lo straforma in un array)
                if(separa[0] == "piu"):
                    ris=float(separa[1])+float(separa[2])#somma
                elif(separa[0] == "meno"):
                    ris=float(separa[1])-float(separa[2])#sottrazione
                elif(separa[0] == "per"):
                    ris=float(separa[1])*float(separa[2])#moltipicazione
                elif(separa[0] == "diviso"):
                    if(separa[2] != "0"):#controlla se il secondo numero è zero
                        ris=float(separa[1])/float(separa[2])#divisione    
                    else:
                        ris ="Divisione per 0 impossibile"
            dati = "Risposta a : " + str(addr_client) + ". Il risultato di: " + separa[1] + " " + separa[0] + " " + separa[2] + " = " + str(ris)
            #mostra la risposta del client e il risultato delle varie operazioni 

            dati = dati.encode()#dati da stringa a binario(decodifica)

            sock_service.send(dati)#invia i dati al client

    sock_service.close()#chiude la sessione con il client

def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        #accetta la richiesta del client e restituisce la socket di servizio e indirizzo del client
        print("\nConnessione ricevuta da %s" % str(addr_client))
        print("Creo un thread per servire le richieste")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
            #fa partire il thread per ricevere i comandi e gli passa la socket e indirizzo del client 
        except:
            print("il thread non si avvia")
            sock_listen.close()


def avvia_server(indirizzo , porta):
    try:
        sock_listen = socket.socket()#crea la socket per ricevere le richieste

        sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#imposta paramentri alla socket

        sock_listen.bind((indirizzo, porta))#associa alla socket un indirizzo e una porta

        sock_listen.listen(5)#lunghezza coda

        print("Server in ascolto su %s. Termina con ko" % str((indirizzo, porta)))
    except socket.error as errore:
        print(f"Qualcosa è andato storto, sto uscendo... \n{errore}")

    ricevi_connessioni(sock_listen) #richiama ricevi_connessioni
if __name__ == '__main__':
    avvia_server(SERVER_ADDRESS, SERVER_PORT) #richiama avvia_server