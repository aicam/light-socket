import socket
import threading
import sys

# check if port number is specified
if len(sys.argv) != 2:
    print("Please enter port number")
    print("python chat.py 123")
    exit(-1)


# Define host and port for the server to listen on
host = '0.0.0.0'  # Use '0.0.0.0' to listen on all available network interfaces
port = int(sys.argv[1])  # You can choose any available port

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections (max 5 clients in the queue)
server_socket.listen(10)

print(f"Server listening on {host}:{port}")

server_running = True
clients = []
servers = []


# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")
    global clients
    clients.append(client_socket)

    global server_running
    while server_running:
        # Receive data from the client
        try:
            data = client_socket.recv(1024)
        except ConnectionAbortedError:
            break
        if not data:
            break
        # Print the received data and sender's IP address
        print(f"Received from {client_address}: {data.decode('utf-8')}")

    # Close the client socket when the client disconnects
    client_socket.close()
    print(f"Connection from {client_address} closed")

def setup_server():
    # Main server loop
    global server_running
    while server_running:
        # Accept incoming connections
        try:
            client_socket, client_address = server_socket.accept()

            # Create a new thread to handle the client
            client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_handler.start()
        except OSError:
            print("All incoming connections terminated!")

def connect_server(address, port):

    global servers
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((address, port))
    servers.append({"socket_obj": client_socket, "address": address, "port": port})
    print(f"Successfully connected to {address}:{port}")

def list_servers():
    global servers
    for i, server in enumerate(servers):
        print(f"{i}: {server['address']}:{server['port']}")

def send_message(id, msg):
    global servers
    servers[id]['socket_obj'].send(msg.encode('utf-8'))

def terminate(id):
    servers[id]['socket_obj'].close()

def terminate_all_clients():
    global clients
    for client in clients:
        client.close()

def myip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print(f"IP Address: {IPAddr}")

def myport():
    local_address, local_port = server_socket.getsockname()
    print(f"Port: {local_port}")

def help():
    print()
    print("help")
    print(" -Display information about the available user interface options or command manual.")
    
    print()
    print("myip")
    print(" -Display the IP address of this process")

    print()
    print("myport")
    print(" -Display the port on which this process is listening for incoming connections.")

    print()
    print("connect <destination> <port no>")
    print(" -Establishes a new TCP connection to the specified <destination> at specified <port no>")
    print("  -<destination>: IP Address")
    print("  -<port no>: Port Number")

    print()
    print("list")
    print(" -Display a numbered list of all conections this process is part of")

    print()
    print("terminate <connection id>")
    print(" -Terminates connection using <connection id>")
    print("  -<connection id>: id of the connection found in 'list' command")

    print()
    print("send <connection id> <message> ")
    print(" -Send <message> to the <connection id>")
    print("  -<connection id>: id of the connection found in 'list' command")
    print("  -<message>: String message to send")
    print("   -Up-to 100 characters long")

    print()


server_handler = threading.Thread(target=setup_server)
server_handler.start()

while True:
    command = input("Command: ")

    if command.__contains__("terminate"):
        try:
            _, id = command.split(' ')
            print(f"Now terminating {id}")
            terminate(int(id))

        except ValueError as e:
            print(f"Error: {e}")
            print("Command: terminate <connection id>")
            print()
        except Exception as e:
            print(f"An exception of type {type(e).__name__} occurred: {e}")
            print()

    if command.__contains__("connect"):
        try:
            _, dst, port = command.split(' ')
            print(f"Trying to connect to {dst}:{port}")
            connect_server(dst, int(port))

        except ValueError as e:
            print(f"Error: {e}")
            print("Command: connect <destination> <port no>")
            print()
        except Exception as e:
            print(f"An exception of type {type(e).__name__} occurred: {e}")
            print()

    if command.__contains__("send"):
        try:
            _, id, msg = command.split(' ')
            print(f"Sending message to id {id}")
            send_message(int(id), msg)
        
        except ValueError as e:
            print(f"Error: {e}")
            print("Command: send <connection id> <message> ")
            print()
        except Exception as e:
            print(f"An exception of type {type(e).__name__} occurred: {e}")
            print()


    if command == "list":
        list_servers()

    if command == "exit":
        terminate_all_clients()
        server_running = False
        server_socket.close()
        server_handler.join()
        break
    
    if command == "help":
        help()
    
    if command == "myip":
        myip()
    
    if command == "myport":
        myport()