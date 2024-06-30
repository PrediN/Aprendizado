from random import randint
from emoji import emojize

print('='*10, 'ADVINHE O NÚMERO', '='*10)
print()
print('Regras:')
print('Escolha um número de 0 a 5')
print('Se você acertar o número você ganhou!')
print()

# Gerador de número aleatório
num = randint(0, 5)

# Coletor de sugestão do jogador
tentativa = int(input('Qual a sua alternativa: '))

# Estrutura condicional
if tentativa==num:
    print()
    print('='*10, 'RESULTADO', '='*10)
    print('O robo escolheu: {}! E você também! Isso significa que:'.format(num))
    print(emojize(':partying_face::partying_face::partying_face: Você acertou!!:partying_face::partying_face::partying_face:'))
    print('='*31)
else:
    print()
    print('='*10, 'RESULTADO', '='*10)
    print('O robo escolheu: {}! E você não. Isso significa que:'.format(num))
    print(emojize(':loudly_crying_face::loudly_crying_face::loudly_crying_face: Você errou!! :loudly_crying_face::loudly_crying_face::loudly_crying_face:'))
    print('='*31)
