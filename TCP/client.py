import socket 


server_ip = input("Please write a server IP: ")
server_port = input("And port: ")


while(True):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port)) # server IP

    data = input("Your message: ")
    sock.sendall(data.encode())

    data = sock.recv(1024)
    print("Received:", data.decode())

    sock.close()




