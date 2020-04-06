import socket


host = ''
serverMessage = 'Thankfully it worked'
port = 5560

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created")
    try:
        s.bind((host,port))
    except socket.error as msg:
        print(msg)

    print("Socket bind complete.")
    return s

def GET():
    return serverMessage

def REPEAT(dataMessage):
    return dataMessage[1]

def MESSAGE(dataMessage):
	reply = input('client: ' + dataMessage[1] + '\n')
	return 'Server: ' + reply

def setupConnection():
    s.listen(2);
    connection, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return connection

def dataTransfer(connection):
    while True:
        data = connection.recv(1024)
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
            s.close()
            break
        elif command == 'MESSAGE':
        	reply = MESSAGE(dataMessage)
        else:
            print('Unknown command')

        connection.sendall(str.encode(reply))
        print('Data has been sent!')
    connection.close();

s = setupServer()

while True:
    try:
        connection = setupConnection()
        dataTransfer(connection)
    except:
        break
