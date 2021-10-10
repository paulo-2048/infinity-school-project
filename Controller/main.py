import imp
codeGeneratorModule = imp.load_source(
    'codeGenarator', 'Model\codeGenerator.py')
connect = imp.load_source('connect', 'Model/connect.py')
connectSales = imp.load_source('salesDB', 'Model/salesDB.py')
saleClass = imp.load_source('sales', 'Model/sales.py')

bank = connect.Connection()
x = bank.connectdb()
print(x)

bankSales = connectSales.Connection_to_manager(bank.con)

# new_sale = saleClass.Sale(
#     codeGeneratorModule.codeGenerator(), 'Produto Teste 2', 4.50, 'Teste')

# verification = bankSales.insertProduct(new_sale)

# verification = bankSales.delete_data('')

# verification = bankSales.update_data(3, 'Deu Certo', 73118277)

# if verification:
#     print('Deu Certo')


y = bankSales.listing()

for i in y:
    print(f'''Code: {i[0]}
Nome: {i[1]}
Preço: {i[2]}
Categoria: {i[4]}
Data e Hora: {i[3]}
    ''')


# Cadastrar vendas

# C:/Users/paulo/Documents/#Desenvolvimento/Outros/Infinity/SalesRow/Model/codeGenerator.py

# 1º tela para menu de cadastrar uma nova venda ou listar as que já tem

# 2º tela para formulário de cadastrar uma nova venda

# 3º tela listar as que já tem

# Nome
# Data
# Preço
# Categoria
