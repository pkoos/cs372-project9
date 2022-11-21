# CS372 Project 9

There are two distinct projects in this repository.

## Project 9.1

There are two parts to this application, `select_server.py` and `select_client.py`.

To run and test the application:

Start the server with the following command: 

    python3 select_server.py [port_num]

or 

    python select_server.py [port_num]

This will create a server on `localhost:[port_num]`. This is the address and port you will use to connect with the client.

Once the server is running, you can create clients. Use the following command: 

    python3 select_client.py [label] [address] [port]

At this point the clients will connect, and send messages to the server.

## Project 9.2

There are no additional requirements to run this project. Use the following command:

    python3 threading_test.py

or 

    python threading_test.py