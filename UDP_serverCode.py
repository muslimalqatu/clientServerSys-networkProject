import socket

# Function to handle communication with a connected client
def handle_client(server_socket):
    while True:
        # Receive data from the client (up to 1024 bytes)
        data, client_address = server_socket.recvfrom(1024)

        # If no data is received, the client has disconnected
        if not data:
            break

        # Modify the data after decoding it from bytes to a string (UTF-8 encoding)
        modified_data = data.decode('utf-8').upper()
        # Send the modified data back to the client after encoding it to bytes
        server_socket.sendto(modified_data.encode('utf-8'), client_address)

        # Print the client's address and the modified data for logging
        print(f"Received data from {client_address}: {data.decode('utf-8')}")
        print(f"Sent modified data to {client_address}: {modified_data}")

# Main function to set up and run the server
def main():
    # Create a UDP socket using IPv4 addressing
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to localhost on port 8081
    server_socket.bind(('127.0.0.1', 8081))

    print("UDP Server listening on port 8081...")

    while True:
        # Handle the client's requests in a separate function
        handle_client(server_socket)

if __name__ == "__main__":
    main()
