import socket
from endereco_ip import endereco_ip

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensagem_envio = input("Digite a mensagem: ")
    cliente.sendto(mensagem_envio.encode(), (endereco_ip, 12000))
    mensagem_bytes, endereco_ip_servidor = cliente.recvfrom(2048)
    print(mensagem_bytes.decode())