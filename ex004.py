var = input('Digite algo:')

print('O que você digitou é: {}'.format(var))
print(type(var))

print('É preenchido com esaços apenas?', var.isspace())
print('É um número?', var.isnumeric())
print('É alfabético?', var.isalpha())
print('É alfanuméico?', var.isalnum())
print('Está em caixa alta?', var.isupper())
print('Esta em caixa baixa?', var.islower())
print('Está capitalizada?', var.istitle())
