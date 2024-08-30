import ipaddress

def obter_rede():
    """Solicita ao usuário a rede principal a ser subdividida."""
    while True:
        try:
            rede = input("Digite a rede (por exemplo, 192.168.1.0/24): ")
            return ipaddress.IPv4Network(rede)
        except ValueError:
            print("Rede inválida. Tente novamente.")

def obter_num_sub_redes():
    """Solicita ao usuário o número de sub-redes desejadas."""
    while True:
        try:
            num_sub_redes = int(input("Digite o número de sub-redes desejadas: "))
            if num_sub_redes > 1:
                return num_sub_redes
            else:
                print("Número de sub-redes deve ser maior que 1.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def calcular_sub_redes(rede, num_sub_redes):
    """Calcula as sub-redes a partir da rede principal."""
    # Determina o prefixo necessário para a quantidade de sub-redes
    novo_prefixo = rede.prefixlen + (num_sub_redes - 1).bit_length()
    sub_redes = list(rede.subnets(new_prefix=novo_prefixo))
    return sub_redes

def exibir_sub_redes(sub_redes):
    """Exibe as informações de cada sub-rede."""
    print(f"\nSubdividindo a rede em {len(sub_redes)} sub-redes:\n")
    for sub_rede in sub_redes:
        print(f"Sub-rede: {sub_rede}")
        print(f"  - Endereço de Rede: {sub_rede.network_address}")
        print(f"  - Primeiro Host: {list(sub_rede.hosts())[0]}")
        print(f"  - Último Host: {list(sub_rede.hosts())[-1]}")
        print(f"  - Endereço de Broadcast: {sub_rede.broadcast_address}")
        print(f"  - Máscara de Sub-rede: {sub_rede.netmask}\n")

def main():
    """Função principal para execução do script."""
    print("Prática: Subdivisão de Redes IP em Sub-redes Menores")
    rede_principal = obter_rede()
    num_sub_redes = obter_num_sub_redes()
    sub_redes = calcular_sub_redes(rede_principal, num_sub_redes)
    exibir_sub_redes(sub_redes)

if __name__ == "__main__":
    main()
