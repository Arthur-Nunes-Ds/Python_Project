import os
import time

#vars:
logins_amarzernes = {
    #"login", "senha"
    "test", "123"
}

def cria_conta():
    print("criar_conta")
    

def login_conta():
    user_login = input("login: ")
    user_senha = input("senha: ")
    user_correct = False
    senha_correct = False
    
    if user_login in logins_amarzernes:
        user_correct = True
    if user_senha in logins_amarzernes:
        senha_correct = True
    
    if user_correct and senha_correct:
        print("liberado o acesso")
    

def incial_erro():
    print("caracter invalido")
    ja_posui_conta = input("vc já tem uma conta? Responda com Y para sim e N para não: ")
    if ja_posui_conta == 'y' or ja_posui_conta == 'Y':
        login_conta()
    elif ja_posui_conta == 'n' or ja_posui_conta == "N":
        cria_conta()
    else:
        incial_erro()

ja_posui_conta = input("vc já tem uma conta? Responda com Y para sim e N para não: ")
if ja_posui_conta == 'y' or ja_posui_conta == 'Y':
    login_conta()
elif ja_posui_conta == 'n' or ja_posui_conta == "N":
    cria_conta()
else:
    incial_erro()



