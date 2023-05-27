# Estudo de métodos mágicos / dunder methods
class Calculadora:

    def __init__(self, valor):
        self.valor = valor

    def __add__(self, outro):
        return self.valor + outro.valor
    
    def __mul__(self, outro):
        return self.valor * outro.valor
    

primeiroValor = Calculadora(4)
segundoValor = Calculadora(4)

soma = primeiroValor + segundoValor
multiplica = primeiroValor * segundoValor

print(soma)
print(multiplica)