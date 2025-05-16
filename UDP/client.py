import socket


server_ip = input("Server IP: ")
server_port = int(input("Server Port: "))

while(True):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input("Message: ")

    sock.sendto(message.encode(), (server_ip, server_port))
    data, _ =  sock.recvfrom(1024)
    print("Received: ", data.decode())
