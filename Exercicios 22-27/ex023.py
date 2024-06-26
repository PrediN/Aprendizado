print('='*10, 'REESCRITOR DE NÚMEROS', '='*10)
print('')

# Inserção de variavel (FUNCIONA APENAS COM 4 DIGITOS! EX: 0001)
#num = str(input('Insira um número qualquer de 0 até 9999: '))

# Impressão de resultados
#print('O número digitado foi: {}'.format(num))
#print('Deste número inserido conseguimos tirar as seguintes informações:')
#print('O número {} é seu milhar.'.format(num[0]))
#print('O número {} é sua centena.'.format(num[1]))
#print('O número {} é sua dezena.'.format(num[2]))
#print('O número {} é sua unidade.'.format(num[3]))


# Método matematico "Correção" para trabalhar de 1 à 4 digitos
num1 = int(input('Informe o número: '))
u = num1//1%10
d = num1//10%10
c = num1//100%10
m = num1//1000%10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
