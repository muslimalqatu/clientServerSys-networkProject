import socket

def tcp_client():
    """TCP client implementation."""
    # Create a TCP/IP socket using IPv4 addressing
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server running on localhost at port 8080
    client_socket.connect(('127.0.0.1', 8080))

    try:
        while True:
            # Prompt the user to enter a line of text
            data = input("Enter a line of characters (or press Enter to exit): ")
            # If the user presses Enter without typing, exit the loop
            if not data:
                break

            # Send the user's input to the server after encoding it to bytes
            client_socket.send(data.encode('utf-8'))

            # Receive the modified data from the server (up to 1024 bytes)
            modified_data = client_socket.recv(1024)
            # Decode the received data from bytes to a string and print it
            print("Modified data received from server:", modified_data.decode('utf-8'))

    finally:
        # Ensure the connection is closed even if an error occurs
        print("Closing TCP connection.")
        client_socket.close()

def udp_client():
    """UDP client implementation."""
    # Create a UDP socket using IPv4 addressing
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Connect to the server running on localhost at port 8080
    server_address = ('127.0.0.1', 8081)

    try:
        while True:
            # Prompt the user to enter a line of text
            data = input("Enter a line of characters (or press Enter to exit): ")
            # If the user presses Enter without typing, exit the loop
            if not data:
                break

            # Send the user's input to the server after encoding it to bytes
            client_socket.sendto(data.encode('utf-8'), server_address)

            # Receive the modified data from the server (up to 1024 bytes)
            modified_data, _ = client_socket.recvfrom(1024)
            # Decode the received data from bytes to a string and print it
            print("Modified data received from server:", modified_data.decode('utf-8'))

    finally:
        # Ensure the connection is closed even if an error occurs
        print("Closing UDP connection.")
        client_socket.close()

def main():
    # Prompt the user to choose a protocol
    protocol = input("Choose a protocol (TCP/UDP): ").strip().upper()

    if protocol == "TCP":
        tcp_client()
    elif protocol == "UDP":
        udp_client()
    else:
        print("Invalid protocol. Please choose TCP or UDP.")

if __name__ == "__main__":
    main()
