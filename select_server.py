# Example usage:
#
# python select_server.py 3490

import sys
import socket
import select

def run_server(port):
    print("Running the server!")
    print(f"{port}")
    server_address = ("localhost", port)

    server_socket = socket.socket()
    server_socket.bind(server_address)
    server_socket.listen()
    while True:
        client, client_addr = server_socket.accept()
        print(f"client: {client} client_addr: {client_addr}")
        break

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
