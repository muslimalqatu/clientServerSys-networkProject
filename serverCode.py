import socket

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        modified_data = data.decode('utf-8').upper()
        client_socket.send(modified_data.encode('utf-8'))

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8080))
    server_socket.listen(1)

    print("Server listening on port 8080...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
