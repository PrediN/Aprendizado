# Impressão de cabeçalho
print('-=-'*10)
print(f"{'PALINDROMO':^30}")
print('-=-'*10)
print()

# Inserção de varivel
frase = str(input('Insira a sua frase aqui: ')).strip().upper().replace(' ', '')
# O tratamento da varaivel acima foi retirar espaços antes e depois da frase, deixar em caixa baixa
# e retirar todos os espaços usando a função .replace(' ', '')

# Essa condicional diz se a frase é igual a frase escrita de trás para frente com o parametro ::-1
if frase == frase[::-1]:
    print('A frase: \033[33m{}'.format(frase))
    print('\033[mÉ a mesma que \033[33m{}'.format(frase[::-1]))
    print('\033[mPortanto é palindromo')
else:
    print('A frase: \033[33m{}'.format(frase))
    print('\033[mNão é a mesma que \033[33m{}'.format(frase[::-1]))
    print('\033[mPortanto não é palidromo')