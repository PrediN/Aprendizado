print('=+'*5, 'CONVERSOR DOLAR E EURO', '+='*5)

# Inserção das variaveis

saldo = float(input('Qual o seu saldo em reais para conversão? '))

# Conversão das moedas

dol = saldo/3.27    # Valor do dólar no exercicio
dola = saldo/5.44   # Valor do dólar na cotação 18/06/2024
euro = saldo/5.84   # Valor do euro na cotação 18/06/2024

# Conversão feita para as moedas correspondentes

print('Seu saldo é R${} em conversão direta você consegue comprar US${:.2f}/US${:.2f} (valor exercicio/valor atual) ou EUR{:.2f}'.format(saldo, dol, dola, euro))