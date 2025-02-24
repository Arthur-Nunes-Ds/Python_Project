import os
import time

logins_amarzernes = {}

def cria_conta():
    user_login = input("digite um login: ")
    user_senha = input("digite uma senha: ")
    if user_login in logins_amarzernes:
        
        print('o "login" já esite')
        input1 = input('deja loga-lo ? Responda com Y para sim e N para não:')

        if input1 == "Y" or "y":
            login_conta()
        elif input1 == "n" or "N":
            print('escolha outro "login" ')
            cria_conta()
    else:
        logins_amarzernes.setdefault(user_login, user_senha)
        login_conta()
            

def login_conta():
    user_login = input("login: ")
    user_senha = input("senha: ")
    user_correct = False
    senha_correct = False
    
    if user_login in logins_amarzernes:
        user_correct = True

    if user_senha in logins_amarzernes:
        if user_senha in logins_amarzernes[user_login]: 
            senha_correct = True
    
    if user_correct and senha_correct:
        print("acesso liberado")
    else:
        print("login/senha incorretas")
        incio_do_programa()
        
def  incio_do_programa():
    ja_posui_conta = input("vc já tem uma conta? Responda com Y para sim e N para não: ")
    if ja_posui_conta == 'y' or ja_posui_conta == 'Y':
        login_conta()
    elif ja_posui_conta == 'n' or ja_posui_conta == "N":
        cria_conta()
    else:
        print("caracter invalido")
        incio_do_programa()

incio_do_programa()
