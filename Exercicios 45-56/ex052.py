# Impressão do cabeçalho
print('-=-' * 10)
print(f"{'NÚMERO PRIMO?':^30}")
print('-=-' * 10)

# Inserção da variável
numero = int(input('Insira aqui um número: '))

# Verificar se o número é primo
eh_primo = True

if numero < 2:
    eh_primo = False
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break

# Exibição do resultado
if eh_primo:
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')
