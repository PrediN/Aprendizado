# Impressão de cabeçalho
print('-=-'*20)
print(f"{'MÉTODO DE PAGAMENTO':^60}")
print('-=-'*20)
print()

# Inserção de variavel de pagamento
print(f'{'-'*30:^60}')
print(f"{'INSIRA O MEIO DE PAGAMENTO':^60}")
print(f"{'À VISTA DINHEIRO - 1':^60}")
print(f"{'À VISTA CARTÃO - 2':^60}")
print(f"{'PARCELADO CARTÃO 2X - 3':^60}")
print(f"{'PARCELADO 3X OU MAIS - 4':^60}")
print(f"{'-'*30:^60}")
print()

# Estrutura de condição
metodo = int(input('Insira o meio de pagamento conforme a legenda: '))
print()

if metodo in [1, 2, 3, 4]:
    if metodo == 1:
        valorCompra = float(input('Insira o valor da compra: R$'))
        compra = valorCompra*0.9
        print(f'Sua compra de \033[31mR${valorCompra:.2f}\033[m ficou por \033[31mR${compra:.2f}\033[m')
        print("Você teve 10% de desconto por fazer pagamento a vista")
    elif metodo == 2:
        valorCompra = float(input('Insira o valor da compra: R$'))
        compra = valorCompra*0.95
        print(f'Sua compra de \033[31mR${valorCompra:.2f}\033[m ficou por \033[31mR${compra:.2f}\033[m')
        print("Você teve 5% de desconto por fazer pagamento a vista no cartão")
    elif metodo == 3:
        valorCompra = float(input('Insira o valor da compra: R$'))
        compra = valorCompra
        print(f'Sua compra de \033[31mR${valorCompra:.2f}\033[m ficou por \033[31mR${compra:.2f}\033[m')
        print("Você não teve desconto por fazer pagamento em 2x no cartão")
    else:
        valorCompra = float(input('Insira o valor da compra: R$'))
        compra = valorCompra*1.2
        print(f'Sua compra de \033[31mR${valorCompra:.2f}\033[m ficou por \033[31mR${compra:.2f}\033[m')
        print("Você teve 20% de juros por fazer pagamento em 3x ou mais no cartão")
else:
    print('Insira um metodo de pagamento válido!')