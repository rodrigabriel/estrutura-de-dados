# Aluno: Gabriel Rodrigues Sousa Silva
# Estrutura de Dados - Fatorial e Fibonacci + custo do algoritmo


# Função para calcular o fatorial, recebe um número
def fat(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fat(n-1)


# Função para calcular a sequência de Fibonacci, receber um número para determinar n elementos
def fibo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seqFibonacci = [0, 1]
        while len(seqFibonacci) < n:
            prox = seqFibonacci[-1] + seqFibonacci[-2]
            seqFibonacci.append(prox)
        return seqFibonacci


# Função que calcula o custo do fatorial
def _custoFatorial(n):
    if n <= 1:
        return 1  # atribuição equivale a 1
    else:
        # laço equivale a 2n | como para esses exemplos é uma função recursiva, caem nesses dois casos (atribuição e laço)
        return n + _custoFatorial(n-1)


# Função que calcula o custo da sequência de Fibonacci
def _custoFibonacci(n):
    if n <= 2:
        return n  # atribuição equivale a 1
    else:
        return 2 + _custoFibonacci(n-1)  # laço equivale a 2n


numerosTeste = [6, 10, 25]

for i in numerosTeste:
    print(f'Fatorial de {i}:')
    fatorial = fat(i)
    print(fatorial)
    custoFatorial = _custoFatorial(i)
    print(f'Custo do algoritmo do fat: {custoFatorial}')

    print(f'\nSequência de Fibonacci até {i}:')
    fibonacci = fibo(i)
    print(fibonacci)
    custoFibonacci = _custoFibonacci(i)
    print(f'Custo do algoritmo da sequência de Fibonacci: {custoFibonacci}')

    print('\n******************\n')
