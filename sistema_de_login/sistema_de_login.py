#info:
    #linguagem: python
    #Feito por: Arthur Nunes de Carvalho
    #objetivo: criar um sistema de login intermetiario usado o python
    #titulo: sitema de login

#bibliotecas
import sys
import os 
import sqlite3
import secrets
import smtplib
import bcrypt
import pandas as pd

#inportando só uma função e a renomeando  
from email.message import EmailMessage
from datetime import datetime, timedelta
from time import sleep as delay
from glob import glob

#const: 
FILE_SISTEM = os.getcwd()

#facilitar ná hora da escrita é de ender o que tá dizendo
def clear():
    #pega o nome do sitema e
    #ver qual é o nome do sitma
    if sys.platform.startswith("win"):
        #aqui é para o windwos 
        delay(2)
        return os.system("cls")
    else:
        #aqui é para o linux e macos
        delay(2)
        return os.system("clear")

def exit(user_input):
    if user_input.upper() in ["EXIT","SAIR"]:
        clear()
        print("ok tachau!!\nok bay!!")
        sys.exit()
    else:
        return 

def verifica_user_email(email, user):
    #conector o python com a db 
    condb = sqlite3.connect("sistema_de_login/tabela_user.db")
    #um objeto para eu boter manipular via SQL o db
    editor_db = condb.cursor()

    #verifica se o USER já existe
    editor_db.execute("SELECT 1 FROM TABELA_USER WHERE USERNAME = ?", (user,))
    login = editor_db.fetchone() is not None
    #verifica se o EMAIL já existe
    editor_db.execute("SELECT 1 FROM TABELA_USER WHERE EMAIL = ?", (email,))
    email = editor_db.fetchone() is not None

    #salva alteração caso aja e fecha o conexão
    condb.close()

    return login, email

def eviar_email(destinatario: str):
    #var
    token = secrets.token_urlsafe(5)
     # dados do remetente
    EMAIL_EMISSOR = '' # <-- email 
    SENHA = ''  # <-- Senha de aplicativo do Google
    #montar o e-mail, estrutura basica
    msg = EmailMessage()
    msg['Subject'] = 'Reset de Senha'
    msg['From'] = EMAIL_EMISSOR
    msg['To'] = destinatario
    # corpo do e-mail, pode ser HTML
    msg.set_content(f"""
    Olá!

    Você solicitou a redefinição da sua senha.

     Aqui está o código para redefinir sua senha:
     {token}

    Este códiem 1 hora.go expira  Se você não solicitou isso, ignore este e-mail.

    Atenciosamente,
    0games7
    """)
    #aqui é para caso ocorra um erro  
    try:
        # conectar ao servidor SMTP do Gmail
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            #"loga na conta"
            smtp.login(EMAIL_EMISSOR, SENHA)  
            #enviar e-mail
            smtp.send_message(msg) 
        print("E-mail enviado com sucesso!")
     #caso acontesa um erro ele informa o erro   
    except Exception as e:
        print("Erro ao enviar e-mail:", e)
    
    expira_em = datetime.now() + timedelta(hours=1)
    while True:
        agora = datetime.now()
        #ver qual é o token e confirma liberando para a redifinição de senha
        user_input = input("insira o código: ")
        exit(user_input)
        if agora > expira_em:
            print("Token expirado! Solicite um novo.")
            return "erro"
        if user_input.upper() == token.upper():
            clear()
            new_senha = input("digite uma nova senha: ")        
            #codificador da senha 
            senha_cripito = str(bcrypt.hashpw(new_senha.encode(encoding="utf-8"), bcrypt.gensalt(8)))
            #caso o 'login'/email não der conflito ele vai salvar no db
            condb = sqlite3.connect("sistema_de_login/tabela_user.db")
            editor_db = condb.cursor()
            #salva tudo na db nás sua derterminadas colunas
            editor_db.execute("UPDATE TABELA_USER SET SENHA = ? WHERE EMAIL = ?", (senha_cripito, destinatario))
            condb.commit()
            condb.close()
            print("senha alterada com sucesso")
            #limpa o terminal e chama a parte de login
            clear()
            break
        else:
            print("código errado")
            return "erro"
    login_conta(0)

def erro_digitacao():
    print("caracter invalido")
    clear()
    return 

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
    exit(user_login)
    user_senha = input("digite uma senha/enter a password: ")
    exit(user_senha)
    user_email = input("digite um e-mail: ")
    exit(user_email)
    login , email = verifica_user_email(user_email,user_login)
    
    #para evitar escrever na db
    if user_senha == "" or user_login == "" or user_email == "":
        print("digite um valor nos campos ") 
        cria_conta()

    #ver se o login ou e-mail já exite na db
    if login or email:
        print("login/e-mail já exite!")
        input1 = input('deja logar ná conta ? Responda com "S" para sim e "N" para não: ')
        print('digite "sair" para finalizar o código')
        #ver se o "input1" = "y/s" ou = "n"
        if input1.upper() in ["S", "Y", "SIM", "YES"]:
            clear()
            #se for sim ele chama a parte de login
            login_conta(0)
        elif input1.upper() in ["NO", "N", "NAO", "NÃO"]:
            #se for não ele chama a parte de criar
            print('escolha outro "login"')
            clear()
            cria_conta()
        elif input1.upper() in ["EXIT","SAIR"]:
            exit(input1)
        else: 
            erro_digitacao()
            login_conta()
    else:
        #codificador da senha 
        senha_cripito = str(bcrypt.hashpw(user_senha.encode(encoding="utf-8"), bcrypt.gensalt(8)))
        #caso o 'login'/email não der conflito ele vai salvar no db
        condb = sqlite3.connect("sistema_de_login/tabela_user.db")
        editor_db = condb.cursor()
        #salva tudo na db nás sua derterminadas colunas
        editor_db.execute("INSERT INTO TABELA_USER (USERNAME, SENHA, EMAIL) VALUES (?, ?, ?)",(user_login, senha_cripito, user_email))
        condb.commit()
        condb.close()
        #limpa o terminal e chama a parte de login
        clear()
        login_conta(0)

def gerenciador_files(is_login = False, user = ""):
   #var-list
    arquivo_list = []
    n_arquivos = []
    #adicisona os nomme do arquivo
    for i in glob('*.*',root_dir="./sistema_de_login/arquivo_protegidos"): arquivo_list.append(i)
    #pasa a qauntidade de idex e adiciona em outra lista
    n_idex_arquivo = len(arquivo_list)
    for f in range(n_idex_arquivo): n_arquivos.append(f)
    #loop
    while True:
        #verifique se o o login é "verdadeiro"
        if is_login == True:
            #mostra qual o usuario fez o login 
            #ler todos os arquivos do diretorio arquivos protegidos 
            print(f"Seja bem vindo: {user}\n")
            #ler todos os arquivos no diretorio e o aplicar na var "arquivo_list"
            #criar uma tabela com os programas
            tabela = pd.DataFrame(arquivo_list, columns=["Arquivos"])
            print(f"{tabela}\n")
            #pega o input do usuario 
            input_user = input("selecione uma opeção: ")
            #criar uma var espesifica para efitar erro de tipo de var
            int_input_user :int = None
            if input_user.isdigit(): int_input_user = int(input_user)
            #ver se o que usuario escrevel é um arquivo presente na pasada "arquivo_protegidos"
            if int_input_user in n_arquivos:
                #ver qual é o sitema operacional(windows, baseado em linux e/ou mac) e escreve o comando correto para abrir o arquivo. 
                #pss: o código está sendo desenvolvido para sistemas descktop
                if sys.platform.startswith("win"): os.system(f"powershell start ./sistema_de_login/arquivo_protegidos/'{arquivo_list[int_input_user]}'")#windwos
                elif sys.platform.startswith("darwin"): os.system(f'cd ./sistema_de_login/arquivo_protegidos && open "{arquivo_list[int_input_user]}"')#mac
                else: os.system(f'cd ./sistema_de_login/arquivo_protegidos && xdg-open "{arquivo_list[int_input_user]}"')#linux
                delay(3)
                clear()
            #verefica se o user deseja deslogar 
            elif input_user.upper() in ["DESLOGAR", 'LOUGAUTE']:
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
            #add os arquivos
            elif input_user.upper() in ["ADICIONAR ARQUIVO", "ADD", "ADD FILE"]:
                input_file = input("Escreva onde está o arquivo: ")
                #aqui é nesario para garantir que o "\", isso é nessario para o comando no terminal e como possilvemte o usario vai digitar
                input_file = (fr"{input_file}")
                #ver se o arquivor exite
                if os.path.isfile(input_file):
                    if sys.platform.startswith("win"): os.system(fr'powershell;  move "{input_file}" "{FILE_SISTEM}\sistema_de_login\arquivo_protegidos"')#win
                    else: os.system(fr'mv "{input_file}" "{FILE_SISTEM}\sistema_de_login\arquivo_protegidos"')#mac e linux
                    #retorno para o user
                    print("arquivo adicionado no sistema com suscesso")
                    delay(2)
                    #para altualizar a tabela 
                    gerenciador_files(is_login, user)
                else:
                    print("Arquivo não existe")
            #ver ser o usuario deseja sair
            elif input_user.upper() in ["EXIT","SAIR"]:
                exit(input_user)
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
    exit(user_login)
    user_senha : str = input("Senha/password: ") 
    exit(user_senha)
    user_correct = False
    senha_correct = False
    
    #conector o python com a db 
    condb = sqlite3.connect("sistema_de_login/tabela_user.db")
    #um objeto para eu boter manipular via SQL o db
    editor_db = condb.cursor()

    editor_db.execute("SELECT SENHA FROM TABELA_USER WHERE USERNAME = ?", (user_login,))
    resultado = editor_db.fetchone()
    condb.close()

    if resultado:
        text = resultado[0] 
        #remove as parte "b'" e á "'" 
        text_modfication = text.replace("b'",""); text_modfication = text_modfication.replace("'","")
        #converte as parte em str para byte
        #isso é nesario pois a biblioteca bcypt pede que os parametros sejam em bytes só que o arquivo .jon não aceita o formato de bytes
        #logo tenho que salva o que o user colocar como str no arquivo json
        byte_senha = text_modfication.encode(); user_senha_crypito = user_senha.encode(encoding="utf-8")
        #verefica se o user digitol a senha certa
        if bcrypt.checkpw(user_senha_crypito, byte_senha):
           senha_correct, user_correct = True 
    else:
        print("usuário não encontrado")

    #verificar o user e senha são verdadeiras
    if user_correct and senha_correct:
        clear()
        print("acesso liberado")
        gerenciador_files(True, user_login)
    else:
        print("login ou senha incorretas")
        input_user = input("vc esqueceu a senha caso? s/n :")
        if input_user.upper() ==  "S":
            if eviar_email() == "erro":
                login_conta(erro + 1)
        else:
            #verefica as tentavias do usario depois de 5 ele finaliza o programa sem  
            #libera para usario
            if erro != 5:
                print(f"Tentativas: {erro}")
                clear()
                #add mais um ponto no erro
                login_conta(erro + 1)
            if erro == 6:
                print("muitas tentativas seguidas") 
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
        exit(ja_posui_conta)
    #ver ser o carter é valido seguindo o padrão ABNT 2
    else: 
        erro_digitacao() 
        init()

init()