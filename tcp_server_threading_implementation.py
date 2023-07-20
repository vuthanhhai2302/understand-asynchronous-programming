import socket
import threading
from datetime import datetime


HOST = '127.0.0.1'
PORT = 12345


def handle_client(socket):
    while True:
        received_data = socket.recv(4096)
        if not received_data:
            break
        socket.sendall(received_data)

    print('Disconnected from ----- ', socket.getpeername(), ' at ', datetime.now())
    socket.close()


def run_server(host, port):
    socket_conn = socket.socket()
    socket_conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_conn.bind((host, port))
    socket_conn.listen()

    while True:
        client_socket, addr = socket_conn.accept()
        print('Connection from   ----- ', addr, ' at ', datetime.now())
        thread = threading.Thread(target=handle_client, args=[client_socket])
        thread.start()


if __name__ == '__main__':
    run_server(HOST, PORT)