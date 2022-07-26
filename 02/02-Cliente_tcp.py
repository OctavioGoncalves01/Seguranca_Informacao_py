from pstats import SortKey
import socket # faz um relacionamento com a placa de rede
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as erro:
        print("Falha na conexão")
        print(f"Erro {erro}")
        sys.exit()
    print("Sockt Criado com sucesso")

    hostAlvo = input("Digite o Host oou ip a ser conectado: ")
    portaAlvo = input("Digite a porta a ser conectada: ")

    try: 
        s.connect((hostAlvo, int(portaAlvo)))
        print(f"Cliente TCP conectado com sucesso no host: {hostAlvo} e na porta: {portaAlvo}")
        s.shutdown(2)
    except socket.error as erro:
        print("Error 404")
        print(f"Erros: {erro}")
        sys.exit()
    
if __name__ == "__main__":
    main()