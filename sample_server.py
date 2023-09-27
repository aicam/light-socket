import socket
import threading

# Define host and port for the server to listen on
host = '127.0.0.0'  # Use '0.0.0.0' to listen on all available network interfaces
port = 12345  # You can choose any available port

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections (max 5 clients in the queue)
server_socket.listen(5)

print(f"Server listening on {host}:{port}")


# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

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


# Main server loop
while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()

    # Create a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
