class Node:
    def __init__(self, jogador):
        self.jogador = jogador
        self.left = None
        self.right = None

class BST:
    def __init__(self, chave_busca):
        self.root = None
        self.chave_busca = chave_busca

    def inserir(self, jogador):
        self.root = self._inserir_recursivo(self.root, jogador)

    def _inserir_recursivo(self, node, jogador):
        if node is None:
            return Node(jogador)

        if jogador[self.chave_busca] < node.jogador[self.chave_busca]:
            node.left = self._inserir_recursivo(node.left, jogador)
        elif jogador[self.chave_busca] > node.jogador[self.chave_busca]:
            node.right = self._inserir_recursivo(node.right, jogador)

        return node

    def buscar(self, valor):
        return self._buscar_recursivo(self.root, valor)

    def _buscar_recursivo(self, node, valor):
        if node is None or node.jogador[self.chave_busca] == valor:
            return node
        if valor < node.jogador[self.chave_busca]:
            return self._buscar_recursivo(node.left, valor)
        return self._buscar_recursivo(node.right, valor)

    def remover(self, valor):
        self.root = self._remover_recursivo(self.root, valor)

    def _remover_recursivo(self, node, valor):
        if node is None:
            return node

        if valor < node.jogador[self.chave_busca]:
            node.left = self._remover_recursivo(node.left, valor)
        elif valor > node.jogador[self.chave_busca]:
            node.right = self._remover_recursivo(node.right, valor)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.jogador = self._min_valor(node.right)
            node.right = self._remover_recursivo(node.right, node.jogador[self.chave_busca])

        return node

    def _min_valor(self, node):
        while node.left is not None:
            node = node.left
        return node.jogador

    def listar_em_ordem(self):
        jogadores = []
        self._listar_em_ordem_recursivo(self.root, jogadores)
        return jogadores

    def _listar_em_ordem_recursivo(self, node, lista):
        if node is not None:
            self._listar_em_ordem_recursivo(node.left, lista)
            lista.append(node.jogador)
            self._listar_em_ordem_recursivo(node.right, lista)

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo de jogador com estatísticas
    jogador1 = {'nome': 'Michael Jordan', 'pontos': 32292, 'rebotes': 6672, 'assistencias': 5633}
    jogador2 = {'nome': 'LeBron James', 'pontos': 35367, 'rebotes': 9885, 'assistencias': 9944}
    jogador3 = {'nome': 'Kobe Bryant', 'pontos': 33643, 'rebotes': 7047, 'assistencias': 6306}

    # Criando a BST usando 'pontos' como chave de busca
    bst = BST(chave_busca='pontos')

    # Inserindo jogadores
    bst.inserir(jogador1)
    bst.inserir(jogador2)
    bst.inserir(jogador3)

    # Buscando jogador com uma quantidade específica de pontos
    busca_jogador = bst.buscar(33643)
    print(f'Jogador encontrado: {busca_jogador.jogador["nome"]}')

    # Removendo um jogador
    bst.remover(35367)

    # Listando jogadores em ordem de pontuação
    jogadores_ordenados = bst.listar_em_ordem()
    print('Jogadores em ordem de pontuação:')
    for jogador in jogadores_ordenados:
        print(f'{jogador["nome"]}: {jogador["pontos"]} pontos')
