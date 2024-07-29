for c in range (1,51):
    # Mais processamento necessário
    # Por iniciar no 1 e ter paço 1 de contagem
    if c%2 == 0:
        print('.')
        print(c, end=' ')

for i in range(2, 51, 2):
    # Menos processamento necessário
    # Por iniciar no 2 e ter paço 2 de contagem
    print('.')
    print(i, end=' ')
