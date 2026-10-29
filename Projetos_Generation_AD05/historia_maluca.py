
# Entrada de dados
nome = input("Digite um nome: ")
profissao = input("Digite uma profissão: ")
adjetivo1 = input("Digite o primeiro adjetivo: ")
adjetivo2 = input("Digite o segundo adjetivo: ")
comida1 = input("Digite a primeira comida: ")
comida2 = input("Digite a segunda comida: ")
sentimento = input("Digite um sentimento: ")

# Montagem e exibição da história
print(
    f"{nome} começou hoje o seu primeiro curso na Generation Brasil. "
    f"Está cursando a formação em {profissao}. "
    f"Achou a sua turma muito {adjetivo1} mas o instrutor era, no mínimo, {adjetivo2}. "
    f"No almoço, comeu {comida1} e {comida2} enquanto revisava as suas anotações. "
    f"Ao final do dia, sente-se {sentimento}, mas tem a determinação de concluir a jornada."
)
