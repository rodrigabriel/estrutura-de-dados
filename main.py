# estrutura de dados 2 - árvore binária
# aluno: Gabriel Rodrigues Sousa Silva


class ArvoreBinaria:

    def __init__(self):
        self.raiz = None
        self.esquerdo = None
        self.direito = None
        self.altura = None
        self.nivel = None
    

#    def inicializa(self, valor):
#        pass


    def adicionar(self, valor):
        if self.raiz == None:
            self.raiz = valor
        else:
            self._verificacaoRecursiva(valor, self.raiz)
        pass


    def _verificacaoRecursiva(self, valor, noAtual):
        if valor < noAtual:
            if self.esquerdo == None:
                self.esquerdo = valor
            else:
                self._verificacaoRecursiva(valor, self.esquerdo)
        else:
            if self.direito == None:
                self.direito = valor
            else:
                self._verificacaoRecursiva(valor, self.direito)


    def remover(self):
        pass


    def imprimeraiz(self):
        print(self.raiz)



no = ArvoreBinaria()

no.adicionar(5)
no.adicionar(7)
no.adicionar(2)
no.imprimeraiz()
print(no.direito)
print(no.esquerdo)