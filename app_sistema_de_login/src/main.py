#info:
    #codigo feito por: Arthur Nunes de Carvalho
    #objetivo: rescrever o código sistema_de_login.py no framework flet  
#importa as bibliotecas e o framework
from time import sleep as delay
import flet as ft
import os 
import bcrypt
import json   


#cria "um dicinorio temporario"
with open("./app_sistema_de_login/dados.json", "r", encoding= "utf-8") as arquivo_lido: 
    user_and_senha = dict(json.load(arquivo_lido))

#sinaliza para o flet aqui é o app
def main(page: ft.Page):
    #vars 
    erro = 1
    #função para cadastra o usario apos o mesmo clicar no botão cadastrar
    def cadastrar(e):
        #pega só o input do user
        login = txt_nome.value
        senha = txt_senha.value
        #ver se o user digito algo 
        if login == "" or senha == "":
            page.add(ft.Text("nem um \"login\" ou senha foi inserido", color="red"))
        #ver se o 'login' já existe 
        elif login in user_and_senha:
            #feedback para o ussuario
            page.add(ft.Text("\"login\" já exite", color="red"))
            #limpe os campos
            txt_nome.value = ""
            txt_senha.value = ""
        else:
            #aqui acontece o processo de criptografia da senha 
            senha_cripito = str(bcrypt.hashpw(senha.encode(encoding="utf-8"), bcrypt.gensalt(8)))
            #add a senha e o usuario no dados.json
            user_and_senha.setdefault(login, senha_cripito)
            with open("./app_sistema_de_login/dados.json", "w") as escrever:
                json.dump(user_and_senha, escrever, indent=2)
            #feedback para o ussuario    
            page.add(ft.Text("usario foi cadastrado com sucesso!!", color="lime"))
            #zera os campos
            txt_nome.value = ""
            txt_senha.value = ""
            page.update()            
    #função para logar com user
    def logar(e):
        #vars
        #é usadao a palavra chave 'nonlocal' para que ele não declara a var
        #é sim modifica-lá
        nonlocal erro 
        login = txt_nome.value
        senha = txt_senha.value
        user_correct = False
        senha_correct = False
        #ver se o user digito algo 
        if login == "" or senha == "":
            page.add(ft.Text("nem um \"login\" ou senha foi inserido", color="red"))
        #ver se o login é se a senha está certa
        elif login in user_and_senha.keys():
            user_correct = True
            #pega a senha cripitada em str
            text = user_and_senha[login]
            #remove as parte "b'" e á "'" 
            text_modfication = text.replace("b'",""); text_modfication = text_modfication.replace("'","")
            #converte as parte em str para byte
            #isso é nesario pois a biblioteca bcypt pede que os parametros sejam em bytes só que o arquivo .jon não aceita o formato de bytes
            #logo tenho que salva o que o user colocar como str no arquivo json
            byte_senha = text_modfication.encode(); user_senha_crypito = senha.encode(encoding="utf-8")
            #verefica se o user digitol a senha certa
            if bcrypt.checkpw(user_senha_crypito, byte_senha): senha_correct = True
            senha = ""
            login = ""
            page.update()
        #ver se ele foi logado corretamente
        if user_correct and senha_correct:
            page.add(ft.Text("acesso liberado", color="lime"))
        else:
            #fala que todos o login e a senha está false
            user_correct = False; senha_correct = False
            page.add(ft.Text("login ou senha incorretas", color="red"))
            #ver quandas tentativas o user tentou logar com a senha/login errado
            if erro < 4:
                page.add(ft.Text(f"Tetativa: {erro}", color="red"))
                erro += 1
            if erro >= 4:
                page.add(ft.Text("MUITAS TENTATIVAS, O PROGRAMA SERA FECHADO EM 3 SEGUNDOS", color="red"))
                #espera 3 segundos para fechar o app apos o aviso
                delay(3)
                #mata o app automaticamento
                page.window.close()
    
    #criar um campo para o user digitar a senha e o login
    txt_nome = ft.TextField(label="Seu Login")
    txt_senha = ft.TextField(label="Sua Senha", password = True, can_reveal_password = True)
    #add para o user os campos de login e criar um botão para cadastrar e login
    page.add(txt_nome,txt_senha, ft.ElevatedButton("cadastrar", on_click=cadastrar), 
             ft.ElevatedButton("logar", on_click=logar))

#inicia o aplicativo
ft.app(main)

