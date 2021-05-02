print('Sistema Lógistico para Dropshipping\nInsira as insformações')

# Informações para salvar no banco de Dados
# date = pegar data do sistema
# user = input('Insira seu nome: ').title()
# office = input('Insira seu nome: ').title()

loop = 'y'
p_resi = 0
p_elet = 0
p_ali = 0

while loop == 'y' or loop == 'Y':
    print('''

++++++++ Menu de Processos ++++++++
*Selecione o número correspondende

1 - Cadastrar Novo Produto,
2 - Editar/Remover Produto,
3 - Listar Produtos Cadastrados,
4 - Adicionar Nova Venda,
5 - Adicionar Nova Despesa,
6 - Fechar Faturamento,
7 - Comparativo em relação às Vendas do Mês Anterior,
8 - Produto mais/menos vendido.

''')
    choice = int(input('Insira o número da função que você quer executar: '))

    while choice not in range(0,10):
        print('')
        print('Dados Incorretos, tente novamente')
        choice = int(input('Insira o número da função que você quer executar: '))


    if choice == 1:
      # Cadastrar Novo Produto
      adicao = 's'
      while adicao == 's':
          print("● Produtos residencias. (1)\n● Equipamentos eletrônicos. (2)\n● Alimentos. (3)")
          p_geral = int(input("Informe a numeração correspondente a categoria do produto para realizar seu cadastro: "))
          if p_geral == 1:
             p_resi += 1
          elif p_geral == 2:
             p_elet += 1
          elif p_geral == 3:
             p_ali += 1
          adicao = input("Deseja cadastrar outro produto? s/n ").lower() 
          print(' ')  

    elif choice == 2:
      # Editar/Remover Produto
      subtracao = 's'
      while subtracao == 's':
          print("● Produtos residenciais. (1)\n● Equipamentos eletrônicos. (2)\n● Alimentos. (3)")
          p_saida = int(input("Para a retirada do produto informe a numeração da sua categoria: "))
          if p_saida == 1:
             p_resi -= 1
          elif p_saida == 2:
             p_elet -= 1
          elif p_saida == 3:
            p_ali -= 1
          subtracao = input("Deseja remover outro produto? s/n ").lower()
          print(' ')

    elif choice == 3:
      # Listar Produtos Cadastrados
      print("Produtos listados em nosso estoque:\n➞ Produtos residenciais: ",p_resi,"\n➞ Equipamentos eletrônicos: ",p_elet,"\n➞ Alimentos: ",p_ali)
      print(' ')
        
    elif choice == 4:
      # Cadastrar Venda
      control = "s"

      while control == "s":
        cod_venda = int(input("Código da Venda: "))
        produto_vendido = input("Nome do Produto: ")
        preco_produto = float(input("Preço Produto: R$"))
        cod_categoria = int(input("Código Categoria: "))
        cod_cliente = int(input("Código do Cliente: "))
        cpf = input("Número CPF: ")
        nome_cliente = ("Nome Completo: ")

        if cod_venda != "" and produto_vendido != "" and cod_categoria != "" and cod_cliente != "":
          print ("Venda cadastrada com sucesso!\n")
          control = input("Deseja continuar outra venda? s/n: \n").lower()
              
    elif choice == 5:
      # Adicionar Nova Despesa
      print("Foram gastos no total esse mês {}".format(10000))
      pass
        
    elif choice == 6:
      # Fechar Faturamento
      print("Seu faturamento foi R${} nesse mês.\nO faturamente líquido chegou a R${}".format(15000,5000))
      pass
        
    elif choice == 7:
      print("Seu faturamento foi {:.2f}% a {} do que no mês anterior".format(15, 'mais'))
        
    elif choice == 8:
      print('''
      Seu produto mais vendido foi {}
      Seu produto menos vendido foi {}'''.format('Máquina de Lavar', 'Pente pra cachorro'))

    else:
        pass 
    
    print(' ')
    loop = input('Deseja voltar ao menu?(y/n): ')
    
print('')
print('Dados Salvos')