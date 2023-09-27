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
connections = []
# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")
    connections.append(client_address)

    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break
        # Print the received data and sender's IP address
        print(f"Received from {client_address}: {data.decode('utf-8')}")

    # Close the client socket when the client disconnects
    client_socket.close()
    print(f"Connection from {client_address} closed")

def setup_server():
    # Main server loop
    while server_running:
        # Accept incoming connections
        client_socket, client_address = server_socket.accept()

        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

server_handler = threading.Thread(target=setup_server)
server_handler.start()

while True:
    command = input("Command: ")
    if command == "exit":
        server_running = False
        server_socket.close()
        server_handler.join()
        break