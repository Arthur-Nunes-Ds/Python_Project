logins_amarzernes = {"a":"b"}

def login_conta():
    print("Login")
    user_login = input("Usuario: ")
    user_senha = input("Senha: ")
    user_correct = False
    senha_correct = False
    tentativas = 0
    print(f'tentativas = {tentativas}')
    if user_login in logins_amarzernes.keys():
        user_correct = True
    
    if user_senha in logins_amarzernes[user_login]: 
        senha_correct = True
    
    if user_correct and senha_correct:
        print("acesso liberado")
        EncodingWarning()
    else:
        print("login/senha incorretas")
        if tentativas == 5:
            print("acesso bloqueado")
            EncodingWarning()
        elif tentativas < 6:
            tentativas += 1
            login_conta()  

login_conta()
        




