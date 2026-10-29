
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

dias_semana = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo",
]

# Data específica
data = datetime.date(2024, 12, 21)
print(data)

# Data atual
hoje = datetime.date.today()
print(hoje)

# Data no formato brasileiro
print(hoje.strftime("%d/%m/%Y"))

# Data completa por extenso
print(
    f"São Paulo, {dias_semana[hoje.weekday()]}, "
    f"{hoje.day} de {meses[hoje.month - 1]} de {hoje.year}"
)

# Verificar se o ano é bissexto
print(f"2024 é Bissexto: {calendar.isleap(2024)}")

# Retornar o último dia do mês
print(f"É o último dia do mês? {calendar.monthrange(2026, 10)[1]}")
