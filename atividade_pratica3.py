# Variaveis
qnt_ml = 0
valor_total = 0
valor_acompanhamentos = 0
valor_feijoada = 0

# Funções

def destaque(frase):  # Destacar uma frase
    print('=' * 33)
    print(f'{frase}')

def volumeFeijoada():  # Exigencia 1/3
    global valor_volume # Variavel global para armazenar valor
    while True:
        try:
            qnt_ml = float(input('Digite a quantidade da porção (em ml) de feijoada que você deseja: '))
            if 300 <= qnt_ml <= 5000:
                valor_volume = qnt_ml * 0.08
                print(f'O valor apenas da porção é: R$ {valor_volume:.2f}')
                break
            else:
                print('Não trabalhamos com quantidades abaixo de 300ml e nem maior que 5L')
                continue
        except ValueError:
            print('Você digitou um valor inválido, tente novamente!')
            continue
    print('=' * 35)
    
def opcaoFeijoada():   # Exigencia 2/3
    # Variaveis global para armazenar valor
    global valor_total  
    global valor_feijoada 
    global multiplicadorOpcao
    
    while True:
        print('Opções de feijoadas')
        print('b - Básica (Feijão, paiol e costelinha)')
        print('p - Premium (Feijão, paiol, costelinha e partes de porco)')
        print('s - Suprema (Feijão, paiol, costelinha, charque, calabresa e bacon)')
        opcaoFeijoada = input('Digite uma opção de feijoada: ')
        
        # Verificar Opções validas e somar valores do multiplicador
        if (opcaoFeijoada == 'b'):  
            destaque('Você escolheu a feijoada básica.')
            multiplicadorOpcao = 1 # Multiplicador Opção
            valor_feijoada = valor_volume * multiplicadorOpcao
        elif (opcaoFeijoada == 'p'):
            destaque('Você escolheu a feijoada premium.')
            multiplicadorOpcao = 1.25 # Multiplicador Opção
            valor_feijoada = valor_volume * multiplicadorOpcao
        elif (opcaoFeijoada == 's'):
            destaque('Você escolheu a feijoada SUPREMA.')
            multiplicadorOpcao = 1.50  # Multiplicador Opção
            valor_feijoada = valor_volume * multiplicadorOpcao
        else:   
            print('Opcão invalida, tente novamente!')
            continue
        break
    
    print(f'Subtotal: R$ {valor_feijoada:.2f}')
    print('=' * 33)
    valor_total += valor_feijoada

def acompanhamentoFeijoada():  # Exigencia 3/3
    # Variaveis global para armazenar valor
    global valor_total 
    global valor_acompanhamentos
    
    while True:
        print('Deseja mais algum acompanhamento?')
        print('0 - Fechar conta (encerrar pedido)')
        print('1 - 200g de arroz ( + R$ 5,00)')
        print('2 - 150g de farofa especial ( + R$ 6,00)')
        print('3 - 100g de couve cozida ( + R$ 7,00)')
        print('4 - 1 laranja descascada ( + R$ 3,00)')
        try:
            escolha = int(input('>> '))  # Verificações com condições para acrescentar valor dos acompanhamentos
            if (escolha == 0):
                break
            elif (escolha == 1):
                valor_acompanhamentos += 5  # Somar valores dos acomapnhamentos
                valor_total += 5
                
            elif (escolha == 2):
                valor_acompanhamentos += 6  # Somar valores dos acomapnhamentos
                valor_total += 6
                
            elif (escolha == 3):
                valor_acompanhamentos += 7  # Somar valores dos acomapnhamentos
                valor_total += 7
                
            elif (escolha == 4):
                valor_acompanhamentos += 3  # Somar valores dos acomapnhamentos
                valor_total += 3
            else: # Caso usuário digitar uma opção invalida, acima de 4 ou abaixo de 0
                print('Opção invalida, tente novamente!')
                print(f'O valor total atual é: R$ {valor_total:.2f}')
                continue
            print(f'O valor total atual é: R$ {valor_total:.2f}')
        except ValueError: # Caso usuário digitar um caractere invalido (letra)
            print('Você digitou um acompanhamento inexistente, tente novamente!')
            print(f'O valor total atual é: R$ {valor_total:.2f}')
            continue

def encerramento():  # Passando os valores finais para o cliente
    print('=' * 43)
    print('Calculando valores, fechando a conta..')
    print('Detalhamento:')
    print(f'Valor do volume: R$ {valor_volume:.2f}')
    print(f'Opção: {multiplicadorOpcao:.2f}')
    print(f'Valor dos acompanhamentos: R$ {valor_acompanhamentos:.2f}')
    print('Pedido finalizado, total a pagar: R$ {:.2f}'.format(valor_total))
    print('=' * 43)

# Menu Feijoada
print(' '* 14 ,'|   Menu Volume de Feijoada    |')
print(' '* 14 ,'================================')

# inicio - boas vindas
dono = 'Jose Gabriel Lopes'
ru = '4181998'
print('=' * 62)
print(f' Bem Vindo ao Restaurante do {dono} - RU: {ru}')
print('=' * 62)

# Chamando funções para rodar o código

volumeFeijoada()
opcaoFeijoada()
acompanhamentoFeijoada()
encerramento()