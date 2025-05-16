# UDP server & client
- **UDP (User Datagram Protocol)** - is a connectionless protocol, messages (datagrams) are sent without a guarantee of delivery and order
- The UDP **server** simply listens to a specific port and processes incoming datagrams
- The **client** sends datagrams to the server IP and port
- There is **no confirmation** mechanism for receipt

## UDP server example 
- Creates a UDP socket
- Binds it to an IP and port
- Receives messages in loop and can send responses

## UDP client example
- Creates a UDP socket
- SEnds messages to the server
- Receives responses (if any)
