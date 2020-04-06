import tkinter as tk
from threading import Thread
import  socket

HOST = '172.16.64.6'
PORT = 5560
HEIGHT = 500
WIDTH = 500

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((HOST,PORT))
print("Connection created")

def sendMessage(event = None):
	command = text.get()
	print('Entered command: ' + command)
	display.insert(tk.END, "Client: " + command)
	if command == 'EXIT':
	    # Send EXIT request to other end
	    mySocket.send(str.encode(command))
	    print("Shutting down the Client.")
	    mySocket.close()
	elif command == 'KILL':
	    # Send KILL command
	    mySocket.send(str.encode(command))
	    print("Disconnected from the Server.")
	else:
		mySocket.send(str.encode("MESSAGE " + command))
	text.set("")

def listenMessage():
	while True:	#if there was no infinite loop, rest of the messages won't have been received.
	    print("Checking for messages")
	    reply = mySocket.recv(1024)
	    receivedMessage = reply.decode('utf-8')
	    print("Received message is " + receivedMessage)
	    display.insert(tk.END, receivedMessage)

root = tk.Tk()
root.title("Client")

#Main frame

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#Background Image

backgroundImage = tk.PhotoImage(file = 'landscape.png')
backgroundLabel = tk.Label(root, image = backgroundImage)
backgroundLabel.place(relwidth = 1, relheight = 1)
print("Created Background")

#Top frame

topframe = tk.Frame(root, bg = 'red')
topframe.place( relx = 0.1, rely = 0.1, relheight = 0.075, relwidth = 0.8)	

text = tk.Entry(topframe, font = 40)
text.bind(sequence = "<Return>", func = sendMessage)
text.place(relwidth = 0.75, relheight = 1)

# the lambda expression creates a link to the function rather than invoking the function and returning its value to the object.

send = tk.Button(topframe, text = 'Send', font = 40, command = sendMessage)
send.place(relx = 0.75, relwidth = 0.25, relheight = 1)

print("Created the top frame")

#Bottom frame

bottomframe = tk.Frame(root, bg = 'blue')
bottomframe.place(relx = 0.1, rely = 0.2, relheight = 0.65, relwidth = 0.8)

scrollbar = tk.Scrollbar(bottomframe)
scrollbar.pack(side = tk.RIGHT,fill = tk.Y)

display = tk.Listbox(bottomframe, font = 40, bg = 'gray', yscrollcommand = scrollbar.set)
display.place(relwidth = 1, relheight = 1)

print("Created the lower frame")

client_receive_thread = Thread(target = listenMessage)
client_receive_thread.start()
root.mainloop()