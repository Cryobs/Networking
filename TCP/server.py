import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 12345))
sock.listen(1)

print("TCP server listening on port 12345...")
while(True):
    conn, addr = sock.accept()
    print(f"Connection from {addr}")
    data = conn.recv(1024)
    print("Received:", data.decode())
    conn.sendall(b"ACK from server")
    conn.close()





