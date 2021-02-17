import socket
import sys


SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

def invia_comandi(sock_service):
    while True:
        try:
            dati = input("Inserisci i dati da inviare (0 per terminare la connessione): ")
        except EOFError:
            print("\nOkay. Exit")
            break
        if not dati:
            print("Non puoi inviare una stringa vuota!")
            continue
        if dati == '0':
            print("Chiudo la connessione con il server!")
            break
        
        dati = dati.encode()#dati da stringa a binario

        sock_service.send(dati)#invio dei dati in binario

        dati = sock_service.recv(2048)#riceve la risposta del server

        if not dati:
            print("Server non risponde. Exit")
            break
        
        dati = dati.decode()#dati da binario a stringa

        print("Ricevuto dal server:")
        print(dati + '\n')

    sock_service.close()#chiudo la connesione

def connessione_server(address, port):
    try:
        s=socket.socket()#crea una socket
        s.connect((address, port))#utilizza la socket per connetersi al server
        print(f"Connessione al Server: {address}:{port}")
    except s.error as errore:
        print(f"Qualcosa è andato storto, sto uscendo... \n{errore}")
        sys.exit()
    invia_comandi(s)#se la conessione è andata a buon fine vieni cheamato invia_comandi

if __name__ == '__main__':
    connessione_server(SERVER_ADDRESS, SERVER_PORT) #richiama connessione_server