import socket

# Function to handle communication with a connected client
def handle_client(client_socket):
    while True:
        # Receive data from the client (up to 1024 bytes)
        data = client_socket.recv(1024)

        # If no data is received, the client has disconnected
        if not data:
            break

        # Modify the data after decoding it from bytes to a string (UTF-8 encoding)
        modified_data = data.decode('utf-8').upper()
        # Send the modified data back to the client after encoding it to bytes
        client_socket.send(modified_data.encode('utf-8'))

    # Close the client socket when the loop ends (client disconnects)
    client_socket.close()

# Main function to set up and run the server
def main():
    # Create a TCP/IP socket using IPv4 addressing
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to localhost on port 8080
    server_socket.bind(('127.0.0.1', 8080))
    # Listen for incoming connections (maximum of 1 connection in the queue)
    server_socket.listen(1)

    print("Server listening on port 8080...")

    while True:
        # Accept a new connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        # Handle the client's requests in a separate function
        handle_client(client_socket)

if __name__ == "__main__":
    main()
