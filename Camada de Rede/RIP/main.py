import copy

class Roteador:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = {}

    def adicionar_vizinho(self, vizinho, custo):
        self.vizinhos[vizinho] = custo

    def __str__(self):
        return f'Roteador({self.nome})'

    def __repr__(self):
        return self.nome  # Para exibir o nome em vez do endereço de memória

class RIP:
    def __init__(self, roteadores):
        self.roteadores = roteadores
        self.tabelas_roteamento = {r.nome: {r.nome: 0} for r in roteadores}  # Usa o nome como chave

    def atualizar_tabelas(self):
        mudou = False
        novas_tabelas = copy.deepcopy(self.tabelas_roteamento)

        for r in self.roteadores:
            for vizinho, custo in r.vizinhos.items():
                for destino, custo_vizinho in self.tabelas_roteamento[vizinho.nome].items():
                    novo_custo = custo + custo_vizinho
                    if destino not in novas_tabelas[r.nome] or novo_custo < novas_tabelas[r.nome][destino]:
                        novas_tabelas[r.nome][destino] = novo_custo
                        mudou = True

        self.tabelas_roteamento = novas_tabelas
        return mudou

    def executar(self):
        convergiu = False
        iteracao = 0
        while not convergiu:
            print(f'Iteração {iteracao}')
            convergiu = not self.atualizar_tabelas()
            for r in self.roteadores:
                print(f'Tabela de roteamento do {r.nome}: {self.tabelas_roteamento[r.nome]}')
            iteracao += 1

if __name__ == "__main__":
    # Cria roteadores
    r1 = Roteador('R1')
    r2 = Roteador('R2')
    r3 = Roteador('R3')
    r4 = Roteador('R4')

    # Define as conexões entre os roteadores (nome e custo)
    r1.adicionar_vizinho(r2, 1)
    r1.adicionar_vizinho(r3, 4)
    r2.adicionar_vizinho(r1, 1)
    r2.adicionar_vizinho(r3, 2)
    r2.adicionar_vizinho(r4, 5)
    r3.adicionar_vizinho(r1, 4)
    r3.adicionar_vizinho(r2, 2)
    r3.adicionar_vizinho(r4, 1)
    r4.adicionar_vizinho(r2, 5)
    r4.adicionar_vizinho(r3, 1)

    # Adiciona os roteadores na simulação
    rip = RIP([r1, r2, r3, r4])
    
    # Executa o algoritmo RIP até convergir
    rip.executar()
