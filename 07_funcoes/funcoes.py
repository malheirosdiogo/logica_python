
# Função sem retorno e sem parâmetros
def sobre():
    print("Desenvolvido por: Diogo Malheiros")

# Função sem retorno, mas com parâmetros
def turma(turma):
    print(f"Turma: {turma}")

# Função com retorno e com parâmetros
def somar(numero1, numero2):
    return numero1 + numero2

sobre()
turma("AD-05")

resultado = somar(10, 5)
print(f"A soma de 10 + 5 = {resultado}")
