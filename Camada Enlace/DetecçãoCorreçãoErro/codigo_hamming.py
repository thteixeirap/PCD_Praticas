import numpy as np

def codificar_hamming(dados):
    """
    Codifica dados usando o Código de Hamming (7,4).
    """
    # Matriz de paridade para o código (7,4)
    matriz_paridade = np.array([[1, 1, 0, 1],
                                [1, 0, 1, 1],
                                [0, 1, 1, 1],
                                [1, 1, 1, 0]])
    
    # Dados devem ter 4 bits
    dados = np.array(dados)
    if len(dados) != 4:
        raise ValueError("Os dados devem ter exatamente 4 bits.")
    
    # Calcula a paridade
    paridade = np.dot(matriz_paridade, dados) % 2
    
    # Retorna os dados concatenados com a paridade (7 bits no total)
    return np.concatenate((dados, paridade))

def decodificar_hamming(codificado):
    """
    Decodifica dados codificados usando o Código de Hamming (7,4) e corrige erros.
    """
    # Matriz de paridade para o código (7,4)
    matriz_paridade = np.array([[1, 1, 0, 1],
                                [1, 0, 1, 1],
                                [0, 1, 1, 1],
                                [1, 1, 1, 0]])
    
    matriz_paridade_T = matriz_paridade.T
    
    # O codificado deve ter 7 bits
    if len(codificado) != 7:
        raise ValueError("O codificado deve ter exatamente 7 bits.")
    
    # Divide os dados codificados em dados e paridade
    dados = codificado[:4]
    paridade = codificado[4:]
    
    # Calcula o vetor de erro
    erro = np.dot(matriz_paridade_T, codificado) % 2
    erro = np.array(erro, dtype=int)
    
    # Corrige o erro se necessário
    erro_pos = int(''.join(map(str, erro)), 2) - 1
    if erro_pos >= 0 and erro_pos < len(codificado):
        print(f'Erro na posição: {erro_pos}')
        codificado[erro_pos] ^= 1  # Corrige o erro
    
    return codificado[:4]

# Teste de Código de Hamming
dados = [1, 0, 0, 1]  # Dados de exemplo
dados_codificados = codificar_hamming(dados)
print('Dados Codificados:', dados_codificados)

# Adiciona um erro para testar a correção
dados_codificados[2] ^= 1  # Introduz um erro para teste
print('Dados Codificados com Erro:', dados_codificados)

dados_corretos = decodificar_hamming(dados_codificados)
print('Dados Corrigidos:', dados_corretos)
