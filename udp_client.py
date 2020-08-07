from socket import *

server_name = '127.0.0.1' # server ip
server_port = 12000

client_sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('input: ')

    client_sock.sendto(msg.encode(), (server_name, server_port))

    modified_msg, server_addr = client_sock.recvfrom(2048)
    print(modified_msg.decode())

client_sock.close()
