from socket import *

server_port = 12000

server_sock = socket(AF_INET, SOCK_DGRAM)
server_sock.bind(('', server_port))

print('the server is ready to receive')

while True:
    msg, client_addr = server_sock.recvfrom(2048)
    print("rcve: ", msg, client_addr)
    msg = msg.decode()
    modified_msg = msg[::-1]
    print("mod: ", modified_msg)
    server_sock.sendto(modified_msg.encode(), client_addr)
    print("sent\n")
