# Variavel de somatoria
s = 0
cont = 0
# Loop para criar a contagem de 1 até 500
for n in range(1,501):
    # Verifica se o número é divisivel por 3 e também é impar
    if n%3 == 0 and n%2 != 0:
        # Somatório do número divisivel por 3 com o montante acumulado
        cont = cont + 1
        s += n
        # Impressão dos resultados n é o número divisivel por 3 e s o somatório atual
        print(f'{n:^10} {s:^10}')
print(f'Seu somátorio deu {s}, o número total de itens somados é {cont}')