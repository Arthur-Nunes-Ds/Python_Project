#bibliotecas
import time
import os
import json

#criar um var q já ler a var "externa"
with open("sistema_de_login/dados.json", "r", encoding= "utf-8") as arquivo_lidor:
        logins_amarzernes = dict(json.load(arquivo_lidor))

def cria_conta():
    #vars já pedindos o input do usario
    user_login = input("digite um login: ")
    user_senha = input("digite uma senha: ")
    
    #verificar se o login foi inserido estiver na var "externa"
    if user_login in logins_amarzernes:
        #se o usario ele executura os seguintes passos

        print('o "login" já esite')
        input1 = input('o "login" já esite /n deja loga-lo ? Responda com Y para sim e N para não:')

        #ver se o "input1" = "y" ou = 'n'
        if input1 == "Y" or "y":
            #se for sim ele chama a parte de login
            login_conta()
        elif input1 == "n" or "N":
            #se for não ele chama a parte de criar
            print('escolha outro "login" ')
            cria_conta()
    else:
        #caso o 'login' não der comflito ele vai salva na var "externa"
        logins_amarzernes.setdefault(user_login, user_senha)
        with open("sistema_de_login/dados.json", "w") as escrever:
            json.dump(logins_amarzernes, escrever, indent=2)
        #limpa o terminal e chama a parte de login
        os.system("cls")
        login_conta()
            

def login_conta():
    print("Login")
    user_login = input("Usuario: ")
    user_senha = input("Senha: ")
    user_correct = False
    senha_correct = False
    

    if user_login in logins_amarzernes.keys():
        user_correct = True
    
    if user_senha in logins_amarzernes[user_login]: 
        senha_correct = True
    
    if user_correct and senha_correct:
        print("acesso liberado")
        EncodingWarning()
    else:
        print("login/senha incorretas")
        incio_do_programa()

def  incio_do_programa():
    print("Seja Bem vindo")
    ja_posui_conta = input("vc já tem uma conta? Responda com Y para sim e N para não: ")
    if ja_posui_conta == 'y' or ja_posui_conta == 'Y':
        login_conta()
    elif ja_posui_conta == 'n' or ja_posui_conta == "N":
        cria_conta()
    else:
        print("caracter invalido")
        incio_do_programa()

incio_do_programa()