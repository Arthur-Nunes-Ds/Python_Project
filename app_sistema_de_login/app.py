import flet as ft
import bcrypt
import json 

with open("app_sistema_de_login/dados.json", "r", encoding= "utf-8") as arquivo_lido: 
    user_and_senha = dict(json.load(arquivo_lido))

def main(page: ft.Page):    
   
    def cadastrar(e):
        login = txt_nome.value
        senha = txt_senha.value 
        if login in user_and_senha:
            page.add(ft.Text("\"login\" já exite"))
            txt_nome.value = ""
            txt_senha.value = ""
            pass
        else:
            senha_cripito = str(bcrypt.hashpw(senha.encode(encoding="utf-8"), bcrypt.gensalt(8)))
            user_and_senha.setdefault(login, senha_cripito)
            with open("app_sistema_de_login/dados.json", "w") as escrever:
                json.dump(user_and_senha, escrever, indent=2)
            escrever(login, senha_cripito)
            page.add(ft.Text("usario foi cadastrado com sucesso!!"))
            txt_nome.value = ""
            txt_senha.value = ""
            pass

    txt_nome = ft.TextField(label="Seu Login")
    txt_senha = ft.TextField(label="Sua Senha", password=True, can_reveal_password=True)
    page.add(txt_nome,txt_senha, ft.ElevatedButton("cadastrar", on_click=cadastrar))

ft.app(main)
