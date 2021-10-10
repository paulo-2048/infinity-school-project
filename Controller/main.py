import imp
codeGeneratorModule = imp.load_source(
    'codeGenarator', 'Model\codeGenerator.py')
connect = imp.load_source('connect', 'Model/connect.py')
connectSales = imp.load_source('salesDB', 'Model/salesDB.py')
saleClass = imp.load_source('sales', 'Model/sales.py')
viewClass = imp.load_source('telaSales', 'View/telaSales.py')

bank = connect.Connection()
x = bank.connectdb()
print(x)

bankSales = connectSales.Connection_to_manager(bank.con)

# def formsGet(view):
#     nameScreen = view.entry1.get()
#     priceScreen = view.entry2.get()
#     categoryScreen = view.entry3.get()
#     return [nameScreen, priceScreen, categoryScreen]


# viewMain = viewClass.MainWindow()
# viewMain.button1['command'] = formsGet(viewMain)
# viewMain.mainloop() 
# print(x)



new_sale = saleClass.Sale(
    codeGeneratorModule.codeGenerator(), 'Produto Teste 2', 4.50, 'Teste')

verificationInsert = bankSales.insertProduct(new_sale)

# verificationDelete = bankSales.delete_data('')

# verificationUpdate = bankSales.update_data(3, 'Teste Único', 73118277)

if verificationInsert:
    print('Inserção Deu Certo')
    
# if verificationDelete:
#     print('Inserção Deu Certo')
    
# if verificationUpdate:
#     print('Inserção Deu Certo')


y = bankSales.listing()
print(y)
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

# 3º tela listar as que já tem
# 2º tela para formulário de cadas

# Nome
# Data
# Preço
# Categoria
