#info:
    #linguagem: python
    #Feito por: Arthur Nunes de Carvalho
    #objetivo: criar um sistema de login intermetiario usado o python
    #titulo: sitema de login

#bibliotecas
import sys
import os 
import json 
import bcrypt
import pandas as pd
#inportando só uma função e a renomeando  
from time import sleep as delay
from glob import glob 

#facilitar ná hora da escrita é de ender o que tá dizendo
def clear():
    #pega o nome do sitema e
    #ver qual é o nome do sitma
    if sys.platform.startswith:
        #aqui é para o windwos 
        delay(2)
        return os.system("cls")
    else:
        #aqui é para o linux e macos
        return os.system("clear")
        
#criar um "var" q já ler a var "externa"
with open("sistema_de_login/dados.json", "r", encoding= "utf-8") as arquivo_lidor:
        logins_amarzernes = dict(json.load(arquivo_lidor))

def cria_conta():
    print("==========================================")
    print("      criar conta/create account")
    print("==========================================")
    print('Não coloca o login/senha como "exit"/"sair"')
    print("==========================================")
    print('digite "sair" para finalizar o código')
    print("==========================================\n")

    #vars já pedindos so input's do usuário
    user_login = input("digite um login/enter a login: ")
    #ver se o user deseja sair do programa
    if user_login.upper() in ["EXIT","SAIR"]:
        clear()
        print("ok tachau!!\nok bay!!")
        sys.exit()

    user_senha = input("digite uma senha/enter a password: ")
    if user_senha.upper() in ["EXIT","SAIR"]:
        clear()
        print("ok tachau!!\nok bay!!")
        sys.exit()
        
    #verificar se o login foi inserido estiver na var "externa"
    if user_login in logins_amarzernes:
        #se o usuário ele executura os seguintes passos

        print('o "login" já existe \n "login" already exists')
        input1 = input('o "login" já exite deja loga-lo ? Responda com "S" para sim e "N" para não\n \
                       Does the "login" site already allow you to log in? Answer with "Y" for yes and "N" for no:')
        print('digite "sair" para finalizar o código')

        #ver se o "input1" = "y/s" ou = "n"
        if input1.upper() in ["S", "Y", "SIM", "YES"]:
            clear()
            #se for sim ele chama a parte de login
            login_conta(0)
        elif input1.upper() in ["NO", "N", "NAO", "NÃO"]:
            #se for não ele chama a parte de criar
            print('escolha outro "login"\n choose another "login"')
            clear()
            cria_conta()
        elif input1.upper() in ["EXIT","SAIR"]:
            clear()
            print("ok tachau!!\nok bay!!")
            sys.exit()
    else:
        #codificador da senha 
        senha_cripito = str(bcrypt.hashpw(user_senha.encode(encoding="utf-8"), bcrypt.gensalt(8)))
        #caso o 'login' não der conflito ele vai salvar na var "externa"
        logins_amarzernes.setdefault(user_login, senha_cripito)
        with open("sistema_de_login/dados.json", "w") as escrever:
            json.dump(logins_amarzernes, escrever, indent=2)
        #limpa o terminal e chama a parte de login
       
        clear()
        login_conta(0)

def gerenciador_files(is_login = False, user = ""):
   #vars
    arquivo_list = []
    #loop
    while True:
        #verifique se o o login é "verdadeiro"
        if is_login == True:
            #mostra qual o usuario fez o login 
            print(f"Seja bem vindo: {user}\n")
            #pega o input do usuario 
            input_user = input("selecione uma opeção: ")
            #ler todos os arquivos do diretorio arquivos protegidos 
            for arquirvo in glob('*.*',root_dir="./sistema_de_login/arquivo_protegidos"):
                #adisona os arquivos ná lista
                arquivo_list.append(arquirvo)
            #verefica se o user deseja deslogar    
            if input_user.upper() in ["DESLOGAR", 'LOUGAUTE']:
                clear()
                #perguntar se o user realmente prente fazer isso
                if input("você realmente deseja sair? ").upper() in ["SIM", "S", "Y", "YES"]:
                    #fala que deu certo deslogar o usario
                    print(f"o user: {user} foi desologado com suceso")
                    is_login = False
                    #nessario para que o código sem quebra
                        #casso o "continue" não tivesse o código irra finalizar aqui é acabou fazendo o user excutar denovo
                        #mas como tem o "continue" então ó código condinua traquilamente
                    continue
                else: gerenciador_files(is_login,user)
            #ver ser o usuario deseja sair
            elif input_user.upper() in ["EXIT","SAIR"]:
                clear()
                print("ok tachau!!\nok bay!!")
                sys.exit()
            #tratamento de erro
            else: 
                print("opeção/comando não reconhecido")
                clear()
                gerenciador_files(is_login,user)
        else: init()

def login_conta(erro:int):
    print("========================")
    print("        Login")
    print("========================")
    print('Para sair escreva "sair"')
    print("========================\n")
    #vars de input ou processo autualizado
    user_login : str = input("Usuario/user: ") 
    if user_login.upper() in ["EXIT","SAIR"]:
        clear()
        print("ok tachau!!\nok bay!!")
        sys.exit()
    user_senha : str = input("Senha/password: ") 
    if user_senha.upper() in ["EXIT","SAIR"]:
        clear()
        print("ok tachau!!\nok bay!!")
        sys.exit()
    user_correct = False
    senha_correct = False
    

    #verificar se o user exite
    if user_login in logins_amarzernes.keys():
        user_correct = True
        #pega a senha cripitada em str
        text = logins_amarzernes[user_login]
        #remove as parte "b'" e á "'" 
        text_modfication = text.replace("b'",""); text_modfication = text_modfication.replace("'","")
        #converte as parte em str para byte
        #isso é nesario pois a biblioteca bcypt pede que os parametros sejam em bytes só que o arquivo .jon não aceita o formato de bytes
        #logo tenho que salva o que o user colocar como str no arquivo json
        byte_senha = text_modfication.encode(); user_senha_crypito = user_senha.encode(encoding="utf-8")
        #verefica se o user digitol a senha certa
        if bcrypt.checkpw(user_senha_crypito, byte_senha):
            senha_correct = True

    #verificar o user e senha são verdadeiras
    if user_correct and senha_correct:
        clear()
        print("acesso liberado/free access\n")
        gerenciador_files(True, user_login)
    else:
        print("login ou senha incorretas/Incorrect login or password")
        #verefica as tentavias do usario depois de 5 ele finaliza o programa sem  
        #libera para usario
        if erro != 5:
            print(f"Tentativas/attempts: {erro}")
            clear()
            #add mais um ponto no erro
            login_conta(erro + 1)
        if erro == 6:
            print("muitas tentativas seguidas\nmany attempts in a row") 
            sys.exit()

def init():
    clear()
    print("========================")
    print("Seja Bem vindo/welcome")
    print("========================")
    print('Para sair escreva "sair"')
    print("========================\n")
    #var input do user se ele já tem uma conta no sistema 
    ja_posui_conta = input("vc já tem uma conta? Responda com S para sim e N para não\nDo you already have an account? Answer with Y for yes and N for no: ")
    #verificar a resposta do user
    if ja_posui_conta.upper() in ["S", "Y", "SIM", "YES"]:
        #limpar o terminal
        clear()
        #chama o bloco de verificar ser user e senha já e talvez o sistema é lierado
        login_conta(0)
    elif ja_posui_conta.upper() in ["NÃO", "NAO", "NO", "N"]:
        clear()
        #chama o bloco de criação de conta
        cria_conta()
    elif ja_posui_conta.upper() in ["SAIR","EXIT"]:
        clear()
        print("ok tachau!!\nok bay!!")
        sys.exit()
    #ver ser o carter é valido seguindo o padrão ABNT 2
    else:
        print("caracter invalido/invalid character")
        clear()
        init()
init()