import socket
import threading

# Função para receber mensagens do servidor
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"[MENSAGEM RECEBIDA]: {message}")
        except:
            print("[ERRO] Conexão perdida.")
            client_socket.close()
            break

# Função principal do cliente
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))

    # Inicia uma thread para receber mensagens do servidor
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Loop para enviar mensagens para o servidor
    while True:
        message = input()
        if message.lower() == 'sair':
            break
        client_socket.send(message.encode())

    client_socket.close()

if __name__ == "__main__":
    main()
