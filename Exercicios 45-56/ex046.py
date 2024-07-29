# Modulos importados para o exercicio
from time import sleep
from emoji import emojize

# Cabeçalho da aplicação
print('-=-'*10)
print(f"{'CONTADOR ANO NOVO':^30}")
print('-=-'*10)

# Interação com o usuario para que ele possa iniciar a contagem
input(f"{'APERTE ENTER PARA INICIAR':^30}")

# Laço for para contagem regressiva
for c in range(10,-1,-1):
    print(f"{c:^30}")
    sleep(1)
print(emojize(f"{':party_popper:FELIZ ANO NOVO!!!:party_popper:':^54}"))