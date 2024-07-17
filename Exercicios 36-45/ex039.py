from datetime import date

# Impressão cabeçalho 1
print('-=-'*10)
print(f"{'DEVO ME ALISTAR?':^30}")
print('-=-'*10)
print()

# Estrutura condicional 1 (se já se alistou)
print('Responda sim ou não')
alistou = str(input('Você já se alistou? ')).strip().lower()

if alistou == 'não':
    # Inserção de variavel
    anoNasceu = int(input('Insira o ano que você nasceu: '))
    print()

    # Importando o ano atual
    dataAtual = date.today().year

    # Calculo idade
    idade = dataAtual - anoNasceu

    # Estrutura condicional 2 (se não se alistou e deve se alistar)
    if idade < 18:
        diferenca = 18-idade
        print(f'Você ainda tem \033[31m{idade}\033[m. Não precisa se alsitar ainda')
        print(f'Você só precisa comparecer a junta daqui \033[31m{diferenca}\033[m anos.')
    elif idade == 18:
        print(f'Você já tem \033[31m{idade}\033[m. Você precisa se apresentar na junta para se alistar!')
    else:
        diferenca = idade - 18
        print(f'Você já passou da idade! Você tem \033[31m{idade}\033[m Você precisa ir na junta se alistar!')
        print(f'Você deveria ter ido à junta militar já faz \033[31m{diferenca}\033[m!')
else:
    print(f'Você já se alistou! Então pode ficar tranquilo!')