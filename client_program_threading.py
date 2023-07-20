import socket
import threading
import time
from datetime import datetime


HOST = 'localhost'
PORT = 12345


def client_socket(client_number):
    messages = ["Hello", "World!"]

    print("Client trying to connect:  -------" + f" CLIENT {client_number}", ' at ', datetime.now())
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Client connect sucesfully: -------" + f" CLIENT {client_number}", ' at ', datetime.now())

    for message in messages:
        time.sleep(1)
        print("\t"* client_number + f"CLIENT {client_number} is sending message: {message}", ' at ', datetime.now())
        client_socket.sendall(message.encode())

        time.sleep(1)
        data = client_socket.recv(1024)
        print("\t"* client_number + f"CLIENT {client_number} received message: {data}", ' at ', datetime.now())

    client_socket.close()
    print("\t"* client_number + f"CLIENT {client_number} is disconnected", ' at ', datetime.now())

num_clients = 3


for client in range(0, num_clients):
    threading.Thread(target=client_socket, args=(client,)).start()
