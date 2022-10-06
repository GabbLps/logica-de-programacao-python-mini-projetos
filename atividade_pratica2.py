# Inicio - Boas vindas
dono = 'Jose Gabriel de Araujo Lopes'
ru = '4181998'
print('=' * 66)
print(f'Bem Vindo a Pizzaria do {dono} - RU: {ru}')
print('=' * 66)

# Cardapio da Pizzaria
print('----------------------------Cardápio------------------------------')
print('|  Código  |  Descrição  |  Pizza Média - M  |  Pizza Grande - G |')
print('|    21    |  Napolitana |         R$ 20,00  |          R$ 26,00 |')
print('|    22    |  Margherita |         R$ 20,00  |          R$ 26,00 |')
print('|    23    |  Calabresa  |         R$ 25,00  |          R$ 32,50 |')
print('|    24    |  Toscana    |         R$ 30,00  |          R$ 39,00 |')
print('|    25    |  Portuguesa |         R$ 30,00  |          R$ 39,00 |')
print('------------------------------------------------------------------')

# Declaração de variaveis
tamanho_pizza = ''
sabor_pizza = ''
codigo_pizza = 0
valor_pizza = 0
valor_total = 0
escolha = 1

# Função entrada e validação do tamanho da pizza
def entradaTamanhoPizza() :
    while True:
        global tamanho_pizza
        tamanho_pizza = str(input('Entre com o tamanho da pizza (M/G): ')).upper()
        if tamanho_pizza != 'M' and tamanho_pizza != 'G' :   
            print('Opção inválida, tente novamente!')
            continue
        else:
            break
    
# Função entrada e validação do código da pizza
def entradaCodigoPizza() :
    while True:
        try:
            global codigo_pizza # variavel global 
            codigo_pizza = int(input('Entre com o código do sabor da pizza: '))
            if codigo_pizza >= 21 and codigo_pizza <= 25 :       
                # Quebrar estrutura de repetição
                break
            else:
                print('Opção inválida, tente novamente!')
                continue
        except ValueError:
            print('Ops, essa opção não existe. Tente novamente!')
        
# Função verificar e retornar codigo do sabor da pizza e também dar o valor da pizza
def retornarCodigoPizza() :
    global codigo_pizza
    global sabor_pizza
    global valor_pizza
    if codigo_pizza == 21:
        sabor_pizza = 'Napolitana'
        valor_pizza = 20
    elif codigo_pizza == 22:
        sabor_pizza = 'Margherita'
        valor_pizza = 20
    elif codigo_pizza == 23:
        sabor_pizza = 'Calabresa'
        valor_pizza = 25
    elif codigo_pizza == 24:
        sabor_pizza = 'Toscana'
        valor_pizza = 30
    elif codigo_pizza == 25:
        sabor_pizza = 'Portuguesa'
        valor_pizza = 30

# Função somar o percentual (30%) amais nas pizzas grandes
def retornarCalculoPizzas() :
    global codigo_pizza
    global tamanho_pizza
    global valor_pizza
    if  tamanho_pizza == 'G':
        valor_pizza = valor_pizza + (valor_pizza * 0.3)

# Função somar cada pizza que for acrescentada no pedido
def somaTudo():
    global valor_total
    global valor_pizza
    valor_total = valor_pizza + valor_total

# Função para fazer mais pedidos de pizza
def maisPedidos():
    global escolha
    print('Deseja fazer outro pedido?')
    print('1 - Sim')
    print('0 - Não')
    escolha = int(input())

# Chamando funções de entradas e retornos
while escolha == 1:
    entradaCodigoPizza()
    entradaTamanhoPizza()
    retornarCodigoPizza()
    retornarCalculoPizzas()
    print('Você pediu uma Pizza', sabor_pizza)
    somaTudo()
    maisPedidos()
    continue

# Fechamento do pedido - Valor final de todas as pizzas
print('Fechando a conta.. Calculando valores..')
print('O total a ser pago é: R$ %.2f' %(valor_total))