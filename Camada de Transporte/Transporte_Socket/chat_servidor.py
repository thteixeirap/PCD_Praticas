import socket
import threading

# Lista de clientes conectados
clientes = []

# Função para lidar com a comunicação com um cliente
def handle_client(client_socket, client_address):
    print(f"[NOVA CONEXÃO] Cliente conectado: {client_address}")
    # Adiciona o cliente à lista
    clientes.append(client_socket)
    while True:
        try:
            # Recebe mensagem do cliente
            message = client_socket.recv(1024).decode()
            if not message:
                break

            print(f"[MENSAGEM] {client_address}: {message}")
            
            # Envia a mensagem para todos os clientes conectados
            broadcast_message(message, client_socket)
        except:
            break
    
    # Remove o cliente da lista e encerra a conexão
    clientes.remove(client_socket)
    client_socket.close()
    print(f"[DESCONECTADO] {client_address} saiu.")

# Função para enviar uma mensagem para todos os clientes conectados
def broadcast_message(message, sender_socket):
    for client in clientes:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                clientes.remove(client)

# Função principal do servidor
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)
    print("[SERVIDOR] Servidor escutando na porta 8080...")

    while True:
        # Aceita novas conexões
        client_socket, client_address = server_socket.accept()
        
        # Inicia uma nova thread para cada cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()
