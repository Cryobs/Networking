# TCP server & client
- **TCP (Transmission Control Protocol)** - is a connection-based protocol that provides reliable, orderly, and error-free delivery of data
- The TCP **server** listens on a specifiv port and waits for the client to connect
- The **client** establishes a connection with the server
- After the connection is estabilished, the parties can exchange data in both directions
- The connection is  closed when the exchange is complete

## TCP server example
- The server creates a socket, binds it to an IP and port
- Listens for incoming connections (`listen()`)
- Accepts a connection (`accept()`)
- In a loop, it accepts messages and responds to the client

## TCP client example
- The client creates s socket
- Connect to the server by IP and port
- In a loop, it sends messages and receive responses 

