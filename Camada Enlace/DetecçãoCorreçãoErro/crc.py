import random

def encode_hamming(data):
    d1, d2, d3, d4 = map(int, data)
    # Calcula os bits de paridade
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4
    return [p1, p2, d1, p3, d2, d3, d4]

def decode_hamming(encoded):
    p1, p2, d1, p3, d2, d3, d4 = map(int, encoded)
    # Calcula os bits de paridade recebidos
    s1 = p1 ^ d1 ^ d2 ^ d4
    s2 = p2 ^ d1 ^ d3 ^ d4
    s3 = p3 ^ d2 ^ d3 ^ d4
    # Calcula a posição do erro
    error_position = s1 * 1 + s2 * 2 + s3 * 4
    
    if error_position != 0:
        if 1 <= error_position <= 7:
            print(f"Error detected at position: {error_position}")
            encoded[error_position - 1] ^= 1  # Corrige o erro
    
    # Retorna o dado decodificado
    return [encoded[2], encoded[4], encoded[5], encoded[6]]

def introduce_errors(encoded, num_errors=1):
    indices = random.sample(range(len(encoded)), num_errors)
    for index in indices:
        encoded[index] ^= 1
    return encoded

def generate_random_data():
    return [str(random.randint(0, 1)) for _ in range(4)]

def main():
    for _ in range(3):  # Testa 3 conjuntos de dados
        data = generate_random_data()
        encoded = encode_hamming(data)
        print(f"Original data: {data}")
        print(f"Encoded data:  {encoded}")

        # Introduz erro aleatório
        encoded_with_error = introduce_errors(encoded, num_errors=random.randint(1, 2))  # 1 ou 2 erros
        print(f"Encoded with error: {encoded_with_error}")

        # Decodifica
        decoded = decode_hamming(encoded_with_error)
        print(f"Decoded data:  {decoded}")
        print(f"Error detected: {decoded == list(map(int, data))}")
        print("=" * 40)

if __name__ == "__main__":
    main()
