import socket
import tkinter as tk
from threading import Thread

HOST = ''
PORT = 5560
ADDR = (HOST, PORT)
BUFFERSIZE = 1024
ADDRESS = 0
NAME = 1

def setupServer():

    #Sets up the server

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created.")
    try:
        mySocket.bind(ADDR)
    except socket.error as errorMessage:
        print(errorMessage)

    print("Socket bind complete.")
    return mySocket

def setupConnection(): 

    #Accepts one connection at a time

    s.listen(2);
    connection, address = mySocket.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return connection

def listenToConnectionRequests(): 

    # Accepts different client connection requests
    # And creates a thread for each connection

    while True:
        client, clientAddr = mySocket.accept()
        print("Connected to: " + clientAddr[0] + ":" + str(address[1]))

        client.send(bytes("Welcome to the papaMuro messenger! Please enter your name",'utf-8'))
        
        addresses[client][ADDRESS] = clientAddr
        Thread(target = handleClient, args = (client,)).start()

def handleClient(client): 

    #Handles a single client connection with the server

    addresses[client][NAME] = client.recv(BUFFERSIZE).decode('utf-8')
    serverMessage = 'Welcome %s! If you ever want to quit, type in KILL.' % addresses[client][NAME]
    client.send(bytes(serverMessage,'utf-8'))
    dataTransfer(client)


def GET():
    return serverMessage

def REPEAT(dataMessage):
    return dataMessage[1]

def MESSAGE(dataMessage):
	reply = input('client: ' + dataMessage[1] + '\n')
	return 'Server: ' + reply

def dataTransfer(connection):

    #Handles the message transfer between the server
    #and the client

    while True:
        data = connection.recv(BUFFERSIZE)
        data = data.decode('utf-8')

        dataMessage = data.split(' ', 1)
        command = dataMessage[0]

        if command == 'GET':
            reply = GET()

        elif command == 'REPEAT':
            reply = REPEAT(dataMessage)
            print('Repeated message was: ' + reply)

        elif command == 'EXIT':
            print("There is no client anymore")
            break

        elif command == 'KILL':
            print('Server is shutting down')
            mySocket.close()
            break

        elif command == 'MESSAGE':
        	reply = MESSAGE(dataMessage)

        else:
            print('Unknown command')

        #connection.sendall(str.encode(reply))
        #print('Data has been sent!')

    connection.close()


mySocket = setupServer()

# while True:
#     try:
#         connection = setupConnection()
#         dataTransfer(connection)
#     except:
#         break

mySocket.listen(5)
print('Waiting for connections...')
LISTEN_THREAD = Thread(target = listenToConnectionRequests)
LISTEN_THREAD.start()
LISTEN_THREAD.join()
mySocket.close()