import datetime
import calendar

meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
]

# 21/12/2024
data = datetime.date(2024, 12, 21)  #Para retornar data (formato americano)
print(data)

hoje = datetime.date.today()  #Para retornar data de hoje (formato americano)
print(hoje)
print(hoje.strftime("%d/%m/%Y"))  #Para retornar formato de data brasileiro
print(f"São Paulo, {hoje.weekday()}, {hoje.day} de {meses[hoje.month - 1]} de {hoje.year}")