#info:
    #codigo feito por: Arthur Nunes de Carvalho
    #objetivo: rescrever o código sistema_de_login.py no framework flet  
#importa as bibliotecas e o framework
import flet as ft
import bcrypt
import json 

#cria "um dicinorio temporario"
with open("app_sistema_de_login/dados.json", "r", encoding= "utf-8") as arquivo_lido: 
    user_and_senha = dict(json.load(arquivo_lido))

#sinaliza para o flet aqui é o app
def main(page: ft.Page):    
    #função para cadastra o usario apos o mesmo clicar no botão cadastrar
    def cadastrar(e):
        #pega só o input do user
        login = txt_nome.value
        senha = txt_senha.value
        #ver se o 'login' já existe 
        if login in user_and_senha:
            #feedback para o ussuario
            page.add(ft.Text("\"login\" já exite"))
            #limpe os campos
            txt_nome.value = ""
            txt_senha.value = ""
            pass
        else:
            #aqui acontece o processo de criptografia da senha 
            senha_cripito = str(bcrypt.hashpw(senha.encode(encoding="utf-8"), bcrypt.gensalt(8)))
            #add a senha e o usuario no dados.json
                ##aqui por aguma rassão acontece o seguinte erro ele inicia e depois o app entra em loop até crashar
                ##ou só não da um retorno para o user
            user_and_senha.setdefault(login, senha_cripito)
            escrever(login, senha_cripito)
            with open("app_sistema_de_login/dados.json", "w") as escrever:
                json.dump(user_and_senha, escrever, indent=2)
            #feedback para o ussuario    
            page.add(ft.Text("usario foi cadastrado com sucesso!!"))
            #zera os campos
            txt_nome.value = ""
            txt_senha.value = ""
            pass
    #criar um campo para o user digitar a senha e o login
    txt_nome = ft.TextField(label="Seu Login")
    txt_senha = ft.TextField(label="Sua Senha", password=True, can_reveal_password=True)
    #add para o user os campos de login e criar um botão para cadastrar o user
    page.add(txt_nome,txt_senha, ft.ElevatedButton("cadastrar", on_click=cadastrar))
#inicia o aplicativo
ft.app(main)
