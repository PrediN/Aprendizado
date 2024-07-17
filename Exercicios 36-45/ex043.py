# Impressão de cabeçalho
print('-=-'*20)
print(f'{'CALCULADORA IMC':^60}')
print('-=-'*20)

# Inserção de variaveis
peso = float(input('Insira o seu peso em kg: '))
altura = int(input('Insira a sua altura em cm: '))
print()

# Calculo do imc
imc = peso/((altura/100)**2)

# Estrutura condicional
if imc < 18.5:
    print(f'Seu IMC é \033[31m{imc:.2f}\033[m. Você esta abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é \033[31m{imc:.2f}\033[m. Você esta no peso ideal.')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é \033[31m{imc:.2f}\033[m. Você esta com sobrepeso.')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é \033[31m{imc:.2f}\033[m. Você esta obeso.')
elif imc >= 40:
    print(f'Seu IMC é \033[31m{imc:.2f}\033[m. Você esta com obesidade mórbida.')