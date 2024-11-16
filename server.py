import socket
import time
import threading
from core import response

# Configuration
PORT = 5050
IP_ADDR = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
LENGTH = 1024

# Switches
connection = False
connected = False

# Global Variables
serverPlugged = None
clients = []

# Function to handle a client
def handle_client(clientSocket, address):
    global connected
    print(f"\nINCOMING CONNECTION [{address}]\n[{address}] CONNECTED TO ZI$CORD")
    clients.append(clientSocket)

    # Sending greeting to the client.
    clientSocket.send(b"WELCOME TO ZI$CORD!")

    while True:
        try:
            data_receive = clientSocket.recv(LENGTH)
            if not data_receive:
                clients.remove(clientSocket)
                print(f"{address} LEFT")
                break

            data_receive = data_receive.decode(FORMAT)
            print(f"\n[{address}] {data_receive}")

            # Closing the connection.
            if data_receive.lower() == "leave":
                server_response = "Goodbye!"
                clientSocket.send(server_response.encode(FORMAT))
                clients.remove(clientSocket)
                print(f"{address} LEFT")
                break
            else:
                # Handling the client's request
                server_response = response(data_receive)
                clientSocket.send(server_response.encode(FORMAT))
                print(f"[ZI$CORD] {server_response}")
        except ConnectionResetError:
            clients.remove(clientSocket)
            print(f"{address} LEFT")
            break
        except:
            print("Something went wrong on the user's end.")
            break

    clientSocket.close()

# Function to handle incoming connections
def powerOn(powered):
    global serverPlugged
    global connection

    while powered:
        try:
            # Creating instance
            serverPlugged = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
            serverPlugged.bind((IP_ADDR, PORT))
            serverPlugged.listen()
            connection = True
            print(f"ZI$CORD PLUGGED IN {IP_ADDR, PORT}")
        except OSError as e:
            print(f"\nFailed to start the server: {e}\nPlease check your internet connection or maybe the port is busy.")
            print("Troubleshooting the problem for you :)")
            time.sleep(30)
            print("\nRESTARTING ZI$CORD")

        while connection:
            try:
                # Accepting connection from client.
                clientConnected, address = serverPlugged.accept()
                threading.Thread(target=handle_client, args=(clientConnected, address)).start()
            except OSError as e:
                print(f"Something went wrong on the user's end: {e}")

# Starting the server
def ziscord():
    choice = input("PRESS [ENTER] TO POWERON ZI$CORD ")
    if choice == '':
        powered = True
    else:
        print("BEAST UN-PLUGGED.")
        return
    powerOn(powered)

ziscord()
