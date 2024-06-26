print('Verificador de primeiras letras do texto')
print('')

# Inserção de variaveis
# (uso de .strip para tirar espaços indesejados e capitalize para pdronizar a busca)
cid = str(input('Qual o nome da cidade: ')).strip().title()

# Metodo para confirmar se o cid da cidade começa por Santo
if cid.find('Santo')== 0:
    print('O nome da cidade de {}, começa com a palavra Santo.'.format(cid))
else:
    print('O nome da cidade {}, não começa com Santo'.format(cid))