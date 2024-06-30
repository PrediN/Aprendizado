from emoji import emojize

print('='*10, 'ANO BISSTEXTO', '='*10)
print()

# Inserção de variavel
ano = int(input('Digite um ano: '))

# Estrutura condicional
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print(emojize('Esse ano é bissexto!:check_mark_button:'))
else:
    print(emojize('Esse ano não é bissexto.:cross_mark:'))