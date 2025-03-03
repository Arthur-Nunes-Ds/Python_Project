#info:
    #======================================================
    #atenção esse codigo está comendado em pt-br e ingles/
    #Attention this code is commanded in pt-br and english
    #======================================================
    #linguagem/language: python
    #Feito por/Made by: Arthur Nunes de Carvalho
    #objetivo: criar um sistema de login intermetiario usado as bibliotecas 'nativas' do python/
    #objective: create an intermediate login system using python'native' libraries
    #titulo: sitema de login/
    #title: login system

#bibliotecas/libraries
    #inportando só uma função e a renomeando/importing just one function and renaming it
from time import sleep as delay
import os 
import json

#facilitar ná hora da escrita é de ender o que tá dizendo/
# making writing easier is understanding what you are saying
def clear():
    #pega o nome do sitema
    #get the system name
    sytem_name = os.name
    #ver qual é o nome do sitma
    #see what the name of the site is
    if os.name == 'posix':
        #aqui é para o codspace(git_hub)
        #here is for codspace(git_hub)
        return os.system("clear")

#criar um var q já ler a var "externa"/create a var that already reads the "external" var
with open("sistema_de_login/dados.json", "r", encoding= "utf-8") as arquivo_lidor:
        logins_amarzernes = dict(json.load(arquivo_lidor))

def cria_conta():
    print("===========================")
    print("criar conta/create account")
    print("===========================")

    #vars já pedindos so input's do usuário/vars already asking for user input
    user_login = input("digite um login/enter a login: ")
    user_senha = input("digite uma senha/enter a password: ")
    
    #verificar se o login foi inserido estiver na var "externa"/check if the login entered is in the "external" var
    if user_login in logins_amarzernes:
        #se o usuário ele executura os seguintes passos/if the user who performs the following steps

        print('o "login" já existe \n "login" already exists')
        input1 = input('o "login" já exite deja loga-lo ? Responda com Y para sim e N para não\nDoes the "login" site already allow you to log in? Answer with Y for yes and N for no:')

        #ver se o "input1" = "y" ou = 'n'/see if "input1" = "y" ou = 'n'
        if input1 == "Y" or "y":
            delay(2)
            clear()
            #se for sim ele chama a parte de login/If yes, it calls the login part
            login_conta(0)
        elif input1 == "n" or "N":
            #se for não ele chama a parte de criar/If it is not, it calls the create part
            print('escolha outro "login"\n choose another "login"')
            delay(2)
            clear()
            cria_conta()
    else:
        #caso o 'login' não der conflito ele vai salvar na var "externa"/
        #if the 'login' does not give conflict it will be saved in the "external" var
        logins_amarzernes.setdefault(user_login, user_senha)
        with open("sistema_de_login/dados.json", "w") as escrever:
            json.dump(logins_amarzernes, escrever, indent=2)
        #limpa o terminal e chama a parte de login/clear the terminal and call the login part
        delay(2)
        clear()
        login_conta(0)
            
def login_conta(erro:int):
    print("======")
    print("Login")
    print("======")
    #vars de input ou processo autualizado/updated input or process stick
    user_login : str = input("Usuario/user: ") 
    user_senha : str = input("Senha/password: ") 
    user_correct = False
    senha_correct = False

    #verificar se o user exite/ check if user exists
    if user_login in logins_amarzernes.keys():
        user_correct = True
    
    if user_correct:
        #verificar a senha do user/ check user password
        if user_senha in logins_amarzernes[user_login]: 
            senha_correct = True
        
    #verificar o user e senha são verdadeiras/ 
    #check the username and password are true
    if user_correct and senha_correct:
        print("acesso liberado/free access")
        #abre ou executa o arquivo "protegido"opens or executes the "protected" file
        #estrutura, *=diretorio ou o que q for executa:/
        #structure, *=directory or whatever executes:
        #os.system("start *")
        os.system("start sistema_de_login/segredo.txt")
        #finaliza o programa/
        #ends the program
        EncodingWarning()
    else:
        print("login ou senha incorretas/Incorrect login or password")
        #verefica as tentavias do usario depois de 5 ele finaliza o programa sem  
        #libera para usario/
        #check the user's attempts after 5 he ends the program without
        #release to user
        if erro != 5:
            print(f"Tentativas/attempts: {erro}")
            delay(2)
            clear()
            #add mais um ponto no erro
            #add one more point to the error
            login_conta(erro + 1)
        if erro == 6:
            print("muitas tentativas seguidas\nmany attempts in a row") 
            EncodingWarning()

def  incio_do_programa():
    print("======================")
    print("Seja Bem vindo/welcome")
    print("======================")
    #var input do user se ele já tem uma conta no sistema 
    #var user input if he already has an account in the system
    ja_posui_conta = input("vc já tem uma conta? Responda com Y para sim e N para não\nDo you already have an account? Answer with Y for yes and N for no:")

    #verificar a resposta do user/
    #check user response
    if ja_posui_conta == 'y' or ja_posui_conta == 'Y':
        #tempo
        delay(2)
        #limpar o terminal/
        #clear the terminal
        clear()
        #chama o bloco de verificar ser user e senha já e talvez o sistema é lierado/
        #calls the block to check if user and password already and maybe the system is read
        login_conta(0)
    elif ja_posui_conta == 'n' or ja_posui_conta == "N":
        delay(2)
        clear()
        #chama o bloco de criação de conta/
        #calls the account creation block
        cria_conta()
    #ver ser o carter é valido seguindo o padrão ABNT 2/
    #see if the character is valid following the ABNT 2 standard
    else:
        print("caracter invalido/invalid character")
        delay(2)
        clear()
        incio_do_programa()

#chama o inicio do codigo
#call the beginning of the code
incio_do_programa()

#oiê, você deve estás se perguntando onde você usar esse código na sua vida, Sinceramente não sei e não me importo, mas tenho algo a dizer ao
#seu doido varido que está lendo esta mensagem, este código foi difícil, então se você puder usá-lo para alguma merda, eu agradeceria. 
# Sério, se você quiser usá-lo para 'esconder' pornografia, eu não sei, estou apenas dados os meu parabéns por você ler esta merda de código. 
#Um beijo na bunda e até man.
#☆*: .｡. o(≧▽≦)o .｡.:*☆

#Hey, you must be wondering where your going to use this code in your life, I honestly don't know and I don't care, but I have something to say 
#to your crazy asshole who is reading this message, this code was difficult, so if you can use it for some shit, I would appreciate it. Seriously, 
#if you want to use it to 'hide' porn, I don't know, I'm just giving you my congratulations for reading this shitty code and comment. A kiss on the ass 
#and see you man.
#☆*: .｡. o(≧▽≦)o .｡.:*☆