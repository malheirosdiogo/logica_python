
# Início

numero = int(input("Digite um número: "))

# Verifica se é múltiplo de 15
if numero % 15 == 0:
    print("FIZZBUZZ")

# Verifica se é múltiplo de 3
elif numero % 3 == 0:
    print("FIZZ")

# Verifica se é múltiplo de 5
elif numero % 5 == 0:
    print("BUZZ")

# Caso não seja múltiplo de 3 ou 5
else:
    print(numero)

# Fim
