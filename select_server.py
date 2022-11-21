# Example usage:
#
# python select_server.py 3490

import sys
import socket
from select import select

RECV_SIZE = 4096
HOSTNAME = "localhost"

def socket_data_string(current_socket, data):
    return f"{current_socket.getpeername()} {len(data)} bytes: {data}"

def disconnect(current_socket, sockets):
    print(f"{current_socket.getpeername()}: disconnected")
    sockets.remove(current_socket)

def get_socket_data(current_socket):
    return current_socket.recv(RECV_SIZE)

def listening_socket_ready(current_socket, server_socket):
    return current_socket == server_socket

def connection_string(client):
    return f"{client.getpeername()}: connected"

def create_client_socket(server_socket):
    client, _ = server_socket.accept()
    return client

def create_listening_socket(address):
    server_socket = socket.socket()
    server_socket.bind(address)
    server_socket.listen()
    return server_socket

def run_server(port):
    print("Running the server!")
    print(f"{port}")
    server_address = (HOSTNAME, port)

    server_socket = create_listening_socket(server_address)

    sockets = { server_socket }
    while True:
        ready_sockets, _, _ = select(sockets, {}, {})
        for ready_sock in ready_sockets:
            if listening_socket_ready(ready_sock, server_socket):
                client = create_client_socket(ready_sock)
                print(f"{connection_string(client)}")
                sockets.add(client)
            else:
                data = get_socket_data(ready_sock)

                if not data:
                    disconnect(ready_sock, sockets)
                else:
                    print(socket_data_string(ready_sock, data))



#--------------------------------#
# Do not modify below this line! #
#--------------------------------#

def usage():
    print("usage: select_server.py port", file=sys.stderr)

def main(argv):
    try:
        port = int(argv[1])
    except:
        usage()
        return 1

    run_server(port)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
