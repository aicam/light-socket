import socket
import time

# Define the server's address and port
server_address = '127.0.0.1'  # Replace with the actual server IP address
server_port = 12345  # Replace with the actual server port

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_address, server_port))

# Send a message to the server
message = "Hello, World!"
client_socket.send(message.encode('utf-8'))
time.sleep(10)
# Close the socket
client_socket.close()
