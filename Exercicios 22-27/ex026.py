print('='*10, 'CONTADOR DE A', '='*10)
print()

# Inserção de variaveis
frase = str(input('Digite uma frase qualquer: ')).strip().upper()

# Lógica para busca de resultados
contA = frase.count('A')
primeiroA = frase.find('A')+1
últimoA = frase.rindex('A')+1

# Impressão de resultados
print()
print('A sua frase "{}"'.format(frase))
print('Tem um total de {} letras A.'.format(contA))
print('Sendo o primeiro na posição {}'.format(primeiroA))
print('E o último na posição {}.'.format(últimoA))
