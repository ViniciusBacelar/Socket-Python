""" 
        Author: Vinicius Bacelar
        Version: 1.0.0
        GitHub: @ViniciusBacelar
"""
import socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(('', 12000))

while True:
    mensagem_bytes, endereco_ip_client = servidor.recvfrom(2048)
    mensagem_resposta = mensagem_bytes.decode()
    servidor.sendto(mensagem_resposta.encode(), endereco_ip_client)
    print(mensagem_resposta)
