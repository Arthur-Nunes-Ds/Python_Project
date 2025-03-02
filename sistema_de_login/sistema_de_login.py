#bibliotecas
import time
import os
import json

#criar um var q já ler a var "externa"
with open("sistema_de_login/dados.json", "r", encoding= "utf-8") as arquivo_lidor:
        logins_amarzernes = dict(json.load(arquivo_lidor))

def cria_conta():
    print("criar conta")

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
            login_conta(0)
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
        print("Login")
        login_conta(0)
            
def login_conta(erro:int):
    #vars de input/processo autualizado
    user_login = input("Usuario: ")
    user_senha = input("Senha: ")
    user_correct = False
    senha_correct = False

    #verefica se user esite
    if user_login in logins_amarzernes.keys():
        user_correct = True
    
    #verifica a senha do user
    if user_senha in logins_amarzernes[user_login]: 
        senha_correct = True
    
    #verefica o user/senha são verdairas
    if user_correct and senha_correct:
        print("acesso liberado")
        #finaliza o programa
        EncodingWarning()
    else:
        print("login/senha incorretas")
        #verefica as tentavias do usario depois de 5 ele finaliza o programa sem  
        #libera para usario
        if erro != 5:
            print(f"Tentativas: {erro}")
            #add mas um ponto no erro
            login_conta(erro + 1)
        if erro == 6:
            print("muitas tentitas seguidas") 
            EncodingWarning()

def  incio_do_programa():
    print("Seja Bem vindo")
    ja_posui_conta = input("vc já tem uma conta? Responda com Y para sim e N para não: ")
    if ja_posui_conta == 'y' or ja_posui_conta == 'Y':
        time.sleep(2)
        os.system("cls")
        login_conta(0)
    elif ja_posui_conta == 'n' or ja_posui_conta == "N":
        time.sleep(2)
        os.system("cls")
        cria_conta()
    else:
        print("caracter invalido")
        time.sleep(2)
        os.system("cls")
        incio_do_programa()

incio_do_programa()
