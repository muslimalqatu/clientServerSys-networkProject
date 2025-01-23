import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8080))

    try:
        while True:
            data = input("Enter a line of characters (or press Enter to exit): ")
            if not data:
                break

            client_socket.send(data.encode('utf-8'))

            modified_data = client_socket.recv(1024)
            print("Modified data received from server:", modified_data.decode('utf-8'))

    finally:
        print("Closing the connection.")
        client_socket.close()

if __name__ == "__main__":
    main()
