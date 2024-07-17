# Jogador de Jokenpô
from random import randint

# Cabeçalho
print('-=-'*10)
print(f'{"Suas jogadas são:":^30}')
print(f'{"1 - Pedra":^30}')
print(f'{"2 - Papel":^30}')
print(f'{"3 - Tesoura":^30}')
print('-=-'*10)

# Inserção de variavel
computador = randint(1, 3)
jogador = int(input('Insira sua jogada: '))
print()

if jogador in [1, 2, 3]:
    if computador == 1:                         # Computador jogando PEDRA
        if jogador ==1:
            print(f'{"Você escolhe pedra":^30}')
            print(f'{"O computador escolhe pedra!":^30}')
            print(f'{"---EMPATE!---":^30}')
        elif jogador == 2:
            print(f'{"Você escolhe papel":^30}')
            print(f'{"O computador escolhe pedra!":^30}')
            print(f'{"---VOCÊ GANHOU!---":^30}')
        else:
            print(f'{"Você escolhe tesoura":^30}')
            print(f'{"O computador escolhe pedra!":^30}')
            print(f'{"---VOCÊ PERDEU!---":^30}')
    elif computador ==2:                        # Computador jogando PAPEL
        if jogador == 1:
            print(f'{"Você escolhe pedra":^30}')
            print(f'{"O computador escolhe papel":^30}')
            print(f'{"---VOCÊ PERDEU!---":^30}')
        elif jogador == 2:
            print(f'{"Você escolhe papel":^30}')
            print(f'{"O computador escolhe papel":^30}')
            print(f'{"---EMPATE!---":^30}')
        else:
            print(f'{"Você escolhe tesoura":^30}')
            print(f'{"O computador escolhe papel":^30}')
            print(f'{"---VOCÊ GANHOU!---":^30}')
    else:                                       # Computador jogando TESOURA
        if jogador == 1:
            print(f'{"Você escolhe pedra":^30}')
            print(f'{"O computador escolhe tesoura":^30}')
            print(f'{"---VOCÊ GANHOU!---":^30}')
        elif jogador == 2:
            print(f'{"Você escolhe papel":^30}')
            print(f'{"O computador escolhe tesoura":^30}')
            print(f'{"---VOCÊ PERDEU!---":^30}')
        else:
            print(f'{"Você escolhe tesoura":^30}')
            print(f'{"O computador escolhe tesoura":^30}')
            print(f'{"---EMPATE!---":^30}')
else:
    print('JOGADA INVÁLIDA')
