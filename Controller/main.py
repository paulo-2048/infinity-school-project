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

new_sale = saleClass.Sale(
    codeGeneratorModule.codeGenerator(), 'Produto Teste', 4.50, 'Limpeza')

bankSales.insertProduct(new_sale)


# Cadastrar vendas

# C:/Users/paulo/Documents/#Desenvolvimento/Outros/Infinity/SalesRow/Model/codeGenerator.py

# 1º tela para menu de cadastrar uma nova venda ou listar as que já tem

# 2º tela para formulário de cadastrar uma nova venda

# 3º tela listar as que já tem

# Nome
# Data
# Preço
# Categoria
