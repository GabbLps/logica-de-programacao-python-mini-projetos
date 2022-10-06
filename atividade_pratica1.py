# inicio - boas vindas
dono = 'Jose Gabriel de Araujo Lopes'
ru = '4181998'
print('==============================================================')
print(f'Bem Vindo a Loja do {dono} - RU: {ru}')
print('==============================================================')

# Entrada dos valores produto e quantidade
valor_produto = float(input('Entre com o valor do produto R$: '))
qnt_produto = int(input('Entre com a quantidade desse produto: '))

# Valor total dos produtos
valor_total = (valor_produto * qnt_produto)

# Validar quantidade/valor digitados
if (qnt_produto <= 0 or valor_produto <= 0):
    print('Valor ou quantidade incorreto. Por favor tente novamente!')
    exit()

# Exigencia - calculo dos descontos
# Ate 4                 -> 0% na unidade
# Entre 5 e 19          -> 3% na unidade
# Entre 20 e 99         -> 6% na unidade
# Maior ou igual a 100  -> 10% na unidade
valor_total_com_desconto = 0
desconto = ''

# Sem desconto
if (qnt_produto <= 4):
    valor_total_com_desconto = valor_total
    desconto = '0%'

# Desconto 3%
elif (qnt_produto >= 5 and qnt_produto <= 19):
    valor_total_com_desconto = valor_total - (valor_total * 0.03)
    desconto = '3%'
    
# Desconto 6%
elif (qnt_produto >= 20 and qnt_produto <= 99):
    valor_total_com_desconto = valor_total - (valor_total * 0.06)
    desconto = '6%'
    
# Desconto 10%
else:
    valor_total_com_desconto = valor_total - (valor_total * 0.1)
    desconto = '10%'

# Retorno das entradas
print('O valor sem desconto foi: %.2f' % (valor_total))
print('O valor com desconto foi: {:.2f}  (desconto {})'.format(valor_total_com_desconto,desconto))

#fim
exit()