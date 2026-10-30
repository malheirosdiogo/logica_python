# Função para somar vários números
def somarmultiplosnumeros(lista):
    soma = 0

    for numero in lista:
        soma += numero

    return soma


# Função para multiplicar vários números
def multiplicarmultiplosnumeros(lista):
    multiplicacao = 1
    
    for numero in lista:
        multiplicacao *= numero

    return multiplicacao


# Função para verificar se um número é par
def ehpar(numero):
    if isinstance(numero, int) and numero % 2 == 0:
        return True
    else:
        return False


# Função para verificar se um número é inteiro
def ehinteiro(numero):
    if isinstance(numero, int):
        return True
    else:
        return False


# TESTES DAS FUNÇÕES

# Função somarmultiplosnumeros
print("SOMA DE MÚLTIPLOS NÚMEROS")

print(somarmultiplosnumeros([5, 10, 15]))

print(somarmultiplosnumeros([0.5, -4, 2]))


# Função multiplicarmultiplosnumeros
print("\nMULTIPLICAÇÃO DE MÚLTIPLOS NÚMEROS")

print(multiplicarmultiplosnumeros([2, 5]))

print(multiplicarmultiplosnumeros([-1, 3, 2.5]))


# Função ehpar
print("\nVERIFICAÇÃO DE NÚMEROS PARES")

print(ehpar(8))

print(ehpar(5))

print(ehpar(2.5))


# Função ehinteiro
print("\nVERIFICAÇÃO DE NÚMEROS INTEIROS")

print(ehinteiro(10))

print(ehinteiro(-6))

print(ehinteiro(4.2))