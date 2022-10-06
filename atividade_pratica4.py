# Declaração de variáveis / listas
listaProdutos = []
codigoProduto = 0

# Funções
#  Função Menu Principal
def menu():
    global codigoProduto
    global opcaoEscolhida
    while True:
        #Verificar opção inexistente com ValueError 
        try: 
            print('Escolha a opcao desejada: ')
            opcao = int(input('1. Cadastrar produto\n'
                              '2. Consultar produto(s)\n'
                              '3. Remover produto\n'
                              '4. Sair\n'
                              '>> '))
            
            # Verficação da opção escolhida 
            if (opcao == 1):  # Se opcao for igual a 1 Cadastra Produto
                codigoProduto += 1
                opcaoEscolhida = 'Cadastrar produto' # variavel opcao recebe esse valor <<<
                print(f'Você escolheu: {opcaoEscolhida}')
                cadastrarProduto(codigoProduto)
                
                
            elif (opcao == 2): # Consultar produtos
                opcaoEscolhida = 'Consultar produto(s)'
                print(f'Você escolheu: {opcaoEscolhida}')
                print('===================================')
                consultarProduto()
                
            elif (opcao == 3):  # Remover produtos
                opcaoEscolhida = 'Remover produto'
                print(f'Você escolheu: {opcaoEscolhida}')
                removerProduto()
                
            elif (opcao == 4):  # Sair do sistema
                opcaoEscolhida = 'Sair \nFazendo logoff do sistema...'  # Encerrando programa
                print(f'Você escolheu: {opcaoEscolhida}')
                exit()
            else: 
                opcaoInvalida()
                continue
            
        except ValueError:
            opcaoInexistente()
            continue
        
        break
    
# Fim Função Menu Principal
    
# ------ Cadastrar produto ------
def cadastrarProduto(codigoProduto): # Exigencia 1/3
    print('--- Cadastro de Produtos ---')
    print(f'Código do produto: {codigoProduto}')
    nome = input('Digite o NOME do produto: ').upper()
    fabricante = input('Digite o FABRICANTE do produto: ').upper()
    valor = float(input('Digite o VALOR(R$) do produto: '))
    dicionarioProduto = {'Código': codigoProduto,
                         'Nome': nome,
                         'Fabricante': fabricante,
                         'Valor': '%.2f'%(valor)}
    listaProdutos.append(dicionarioProduto.copy())
    
    print(f'Nome do produto: {nome}\n'
          f'Fabricante do produto: {fabricante}\n'
          f'Valor do produto: {valor:.2f}')
    print('Produto cadastrado com sucesso!')
    print('===============================')
    menu()
    
# ------- Fim Cadastrar Produto ------- #
    
# ------- Consultar Produto ------- #
def consultarProduto():  # Exigencia 2/3
    print('--- Consulta de Produtos ---')
    while True:
        print('Escolha a opcao desejada: ')
        try:
            opcao = int(input('1. Consultar Todos os Produtos\n'
                                '2. Consultar Produtos por Código\n'
                                '3. Consultar Produtos por Fabricante\n'
                                '4. Retornar\n'
                                '>> '))
            if (opcao == 1): # Consultar TODOS
                print(f'Você escolheu: {opcaoEscolhida}')
                print('=========================')
                for produto in listaProdutos: # Percorrer cada item da minha lista de produtos
                    for key, value in produto.items(): # Percorrer cada conjunto chave/valor do dicionario que é a lista de produtos
                        print(f'{key}: {value}')  # Printar na tela a chave e o valor, assim consultando todos os produtos
                    print('=========================')
                
            elif (opcao == 2): # Consultar por CÓDIGO
                print(f'Você escolheu: {opcaoEscolhida}')
                print('===================================')
                entradaCodigoProduto = int(input('Digite o Código do Produto: '))
                for produto in listaProdutos: # Percorrer cada item da minha lista de produtos
                    if (produto['Código'] == entradaCodigoProduto):  # Verificar se a entrada é igual ao código para imprimir as informações de acordo com código
                        for key, value in produto.items():
                            print(f'{key}: {value}')
                        print('===================================')

            elif (opcao == 3):  # Consultar por FABRICANTE
                print(f'Você escolheu: {opcaoEscolhida}')
                print('===================================')
                entradaFabricanteProduto = (input('Digite o Fabricante do Produto: ')).upper()
                for produto in listaProdutos: # Percorrer cada item da minha lista de produtos
                    if (produto['Fabricante'] == entradaFabricanteProduto): # Verificar se a entrada é igual ao fabricante para imprimir informações de acordo com fabricante
                        for key, value in produto.items():
                            print(f'{key}: {value}')
                        print('===================================')
                
            elif (opcao == 4): # Retornar ao menu
                print(f'Você escolheu: Retornar \nVoltando ao menu principal..')
                print('================================')
                menu()

            else:
                opcaoInvalida()
                continue
                
        except ValueError:
            opcaoInexistente()
            continue

# ------- Fim Consultar Produto ------- #

# ------- Remover Produto ------- #
def removerProduto():    # Exigencia 3/3
    print('--- Remoção de Produtos ---')
    while True:
        try:
            codigoExcluir=int(input('Digite o código do produto que deseja excluir: '))  # codigo do produto a ser removido
            for produto in listaProdutos:
                if produto['Código'] == codigoExcluir:
                    listaProdutos.remove(produto)
                    print('Produto excluído com sucesso!')

        except ValueError:
            opcaoInexistente()
        menu()
# ------- Fim Remover Produto ------- #

# ------ Início Funções básicas de deixar código mais legível ------

def opcaoInexistente(): 
    print('Opção inexistente, tente novamente!')
    print('===================================')
    
def opcaoInvalida(): 
    print('Opção inválida, tente novamente!')
    print('================================')

# ------ Fim Funções de código mais legível ------


# Inicio Main  
# boas vindas/identificador pessoal
print('=' * 70)
print('Bem vindo ao Sistema Controle de Estoque do José Gabriel - RU: 4181998')  
print('=' * 70)
menu()

# Fim