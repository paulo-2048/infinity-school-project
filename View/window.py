from os import system
from tkinter import *
from colorama import init, Fore, Back, Style
from getpass import getpass
import stdiomask
from time import sleep

init(autoreset=True)

# CRIAR O MENU DE OPÇÕES


def exibir_menu():
    print(Fore.GREEN + '''Seja bem vindo ao projeto
         Sistema de Login
Escolha uma opção:
[1] CADASTRAR NOVO PRODUTO
[2] CATEGORIA
[3] QUANTIDADE
[4] COMPRAR
[5] CANCELAR
[6] SAIR
''')
    opcao = int(input('Digite sua opção: '))
    return(opcao)

# CADASTRAR PRODUTO


def cadastrar_produto():
    produto = input('Nome do produto: ')
    senha = stdiomask.getpass(prompt='Senha: ', mask='')
    return(login, senha)
#senha = stdiomask.getpass(prompt='Senha: ', mask='*')

# PESQUISAR NO ARQUIVO USUÁRIOS.TXT


def buscar_usuario(Login, senha):
    usuarios = []
    try:
        with open('usuarios.txt', 'r+', encoding='Utf-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(",")
                usuarios.append(linha.split())
        #LOGIN, SENHA = fazer_login()
            for usuario in usuarios:
                nome = usuario[0]
                password = usuario[1]
                if Login == nome and senha == password:
                    return True
    except FileNotFoundError:
        return False


while True:
    system('cls')
    opcao = exibir_menu()

    if opcao == 1:
        # CADASTRAR USUÁRIO
        login, senha = fazer_login()
        if login == senha:
            print('Por questões de segurança sua senha não pode ser igual ao login.')
            senha = getpass('Senha: ')
        user = buscar_usuario()
        if user == True:
            print(Fore.RED + 'Usuário já existe.')
            sleep(2)
            # EXIT()
        else:
            with open('usuarios.txt', 'a+', enconding='Utf-8', newline='')
            arquivo.writelines(f'{login}{senha}\n')
            print(Fore.CYAN + 'Cadastro aprvado!')
            exit()

    elif opcao == 2:
        # FAZER O LOGIN DO USUÁRIO
        login, senha = fazer_login()
        user = buscar_usuario(login, senha)
        if user == True:
            print(Fore.CYAN + 'Login realizado com sucesso!')
            sleep(1)
            exit()
        else:
            print(
                Fore.RED + 'Você deve ter digitado o nome de usuário ou senha errado.\n Por favor, verifique!')
            sleep(2)
    else:
        system('cls')
        print(Fore.LIGHTMAGENTA_EX + 'Goodbye!')
        break
