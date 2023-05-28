# estrutura de dados 2 - árvore binária
# aluno: Gabriel Rodrigues Sousa Silva


class No: # Necessário para não ter congestionamento/conflito entre os nós.

    def __init__(self, valor):
        self.valor = valor
        self.esquerdo = None
        self.direito = None


class ArvoreBinaria:

    def __init__(self):
        self.raiz = None

    def adicionar(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self._recursaoDeInsercao(valor, self.raiz)


    def _recursaoDeInsercao(self, valor, noAtual): # Método auxiliar
        if valor < noAtual.valor: # noAtual.valor -> acessa o valor do momento, que foi inserido no método principal de adicionar
            if noAtual.esquerdo is None:
                noAtual.esquerdo = No(valor)
            else:
                self._recursaoDeInsercao(valor, noAtual.esquerdo)
        else:
            if noAtual.direito is None:
                noAtual.direito = No(valor)
            else:
                self._recursaoDeInsercao(valor, noAtual.direito)
            

    def imprimirInOrdem(self):
        print('Impressão in ordem:')
        self._recursaoInOrdem(self.raiz)


    def _recursaoInOrdem(self, noAtual):
        if noAtual is not None:
            self._recursaoInOrdem(noAtual.esquerdo)
            print(noAtual.valor)
            self._recursaoInOrdem(noAtual.direito)


    def remover(self, valor):
        pass


arvore = ArvoreBinaria()

arvore.adicionar(5)
arvore.adicionar(8)
arvore.adicionar(1)
arvore.adicionar(7)
arvore.adicionar(6)


arvore.imprimirInOrdem()
print('\n')


"""
# ANOTAÇÕES:
Ajustando a empressão pré ordem

TO-DO:
Estabelecer critério de inserção. Não pode ser adicionado itens repetidos.
Organizar impressão pré ordem e pós ordem
"""