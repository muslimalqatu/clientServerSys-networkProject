# Client/Server system NetworkProject

This project demonstrates a simple server-client communication system using both TCP and UDP protocols.

## Files
- `clientCode.py`: The client program that choose the protocol (TCP or UDP) and sends input data to the server and displays the response.
- `TCP_serverCode.py`: The TCP server program that receives data from the client, modifies it to uppercase, and sends it back.
- `UDP_serverCode.py`: The UDP server program that receives data from the client, modifies it to uppercase, and sends it back.

## Key Differences Between TCP and UDP
- **TCP**: Reliable, connection-oriented, ensures data integrity.
- **UDP**: Faster, connectionless, no guarantee of delivery.

## How to run
1. First, run the TCP server:  
   `python TCP_serverCode.py`
2. Then, run the UDP server:  
   `python UDP_serverCode.py`
3. Finally, run the client:  
   `python clientCode.py`

## Technologies Used
- Python
- Socket Programming

## Purpose
This project demonstrates basic concepts of socket programming and client-server communication. It shows how to establish a connection, send and receive data, and modify data in the server before sending it back to the client.
