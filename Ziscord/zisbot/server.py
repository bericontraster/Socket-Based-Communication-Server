# Importing libs
import socket
import subprocess
import sys
from chatbot import response


# Configuration
PORT = 5050
IP_ADDR = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
LENGTH = 1024

# Variables
connection = True
connected = True

# Creting Instance
server_instance = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Creating tunnel
server_instance.bind((IP_ADDR, PORT))
print(f"Server is listening on {IP_ADDR, PORT}")
server_instance.listen()


while connection:
    # Accepting connection from client.
    connection_object, _ = server_instance.accept()
    print(f"Incoming connection from {connection_object}\n {connection_object} Connected")
    
    # Sending greeting to the client.
    connection_object.send(b"Welcome to Ziscord!")
    data_receive = connection_object.recv(LENGTH)
    print("I RAN")
    connected = True

    while connected:
        print("{}: {}".format("[CLIENT]", data_receive.decode(FORMAT)))
         # Closing the connection.
        if data_receive.decode(FORMAT) == "leave":
            try:
                # print("T1")
                server_response = "leaving"
                connection_object.send(server_response.encode(FORMAT))
                connection_object.close()
                print(f"{connection_object} LEFT")
                connected = False
            except:
                # print("E1")
                print(f"{connection_object} DISCONNECTED")
                connected = False
        else:
            try:
                # print("T2")
                # Keeping the connection alive.
                # server_response = "WORKING!"
                data_receive = data_receive.decode(FORMAT)
                print(data_receive)
                server_response = response(data_receive)
                connection_object.send(server_response.encode(FORMAT))
                print(f"[ZI$CORD] {server_response}")
                data_receive = connection_object.recv(LENGTH)
            except:
                # print("E2")
                print(f"{connection_object} DISCONNECTED")
                connection_object.close()
                connected = False