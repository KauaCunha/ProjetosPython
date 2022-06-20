from http import client
import threading
import socket

clients = []

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 50001))
        server.listen()
        print('Servidor Iniciado')
    except:
        return print('\nNão foi possivel iniciar o SERVER.\n')

    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target=messagesTratament, args=[client])
        thread.start()

def messagesTratament(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break


def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)


def deleteClient(client):
    clients.remove(client)


main()