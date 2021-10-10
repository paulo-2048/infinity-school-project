from tkinter import *
from tkinter import messagebox
from tkinter.font import Font


class addSales(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)
        fontStyle = Font(family="Poppins", size=20)

        # Configuração da janela principal
        self.title('Primeira Janela')
        self.configure(background='#000')
        self.geometry('480x240')
        
        texto1=Label(self, text='Formulário para Adição', background='#000', foreground= '#aa5090', font=fontStyle)
        texto1.grid(row=0,column=0)
        
        label1=Label(self, text='Nome do Produto:', background='#000', foreground= '#aa5090')
        entry1=Entry(self, background='#000', foreground= '#aa5090')
        
        label1.grid(row=1,column=0)
        entry1.grid(row=1,column=1)
        
        label2=Label(self, text='Preço do Produto:', background='#000', foreground= '#aa5090')
        entry2=Entry(self, background='#000', foreground= '#aa5090')
        
        label2.grid(row=2,column=0)
        entry2.grid(row=2,column=1)
        
        label3=Label(self, text='Categoria do Produto:', background='#000', foreground= '#aa5090')
        entry3=Entry(self, background='#000', foreground= '#aa5090')
        
        label3.grid(row=3,column=0)
        entry3.grid(row=3,column=1)
        
        button1 = Button(self, text='Enviar', bg='Salmon', fg='Black', activebackground='Gold', activeforeground='Black')
        button1.grid(row=4, column=0)


class listingSales(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Segunda Janela')
        self.configure(background='darkgray')
        self.geometry('480x240')


class updateSales(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Terceira Janela')
        self.configure(background='yellow')
        self.geometry('480x240')
        
class deleteSales(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Quarta Janela')
        self.configure(background='yellow')
        self.geometry('480x240')


class MainWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, master=None)

        # Configuração da janela principal
        self.master.title('Janela Principal')
        self.master.geometry('480x240')
        self.configure(borderwidth=4)
        self.configure(background='white')

        for name in ("Adicionar Venda", "Listar Vendas", "Editar Vendas", 'Excluir Vendas'):
            self.button = Button(self, text=name)
            self.button.bind("<Button-1>", self.handle_event)
            self.button.pack(side='left', fill='x', expand=True)

        # Empacotamos o frame principal
        self.pack(fill='both', expand=True)

    def handle_event(self, event):
        btn_name = event.widget.cget('text')
        if btn_name == 'Adicionar Venda':
            window = addSales()
        if btn_name == 'Listar Vendas':
            window = listingSales()
        if btn_name == 'Editar Vendas':
            window = updateSales()
        if btn_name == 'Excluir Vendas':
            window = deleteSales()

        window.mainloop()


# if __name__ == '__main__':
#     mainWindow = MainWindow()
#     mainWindow.mainloop() 