#import sqlite3
#user = "test"
##senha = "'oiuer8320"
#condb = sqlite3.connect("test_db.db")
#edidor_sql = condb.cursor()
#edidor_sql.execute("SELECT USER, SENHA FROM LOGIN WHERE USER = ?", (user,))
#resultado = edidor_sql.fetchone()
##edidor_sql.execute("INSERT INTO LOGIN (USER, SENHA) VALUES (?,?)", (user,senha))
##condb.commit()
#condb.close()

import smtplib
import secrets
from email.message import EmailMessage
#token = secrets.token_hex(16)#<- talvez em linck de recuperção
#token = secrets.token_urlsafe(16) #<-- melhor para user digitar
token = secrets.randbelow(100) # <-- melhor pois gere um valor entre 0 e 100
def enviar_email(destinatario):
    # Dados do remetente
    EMAIL_EMISSOR = 'arthurnunescarvalho2@gmail.com'
    SENHA = 'bdul mfpi ogwx qobk'  # Senha de aplicativo do Gmail
    #Montar o e-mail
    msg = EmailMessage()
    msg['Subject'] = 'Reset de Senha'
    msg['From'] = EMAIL_EMISSOR
    msg['To'] = destinatario
    # Corpo do e-mail (pode ser texto simples ou HTML)
    msg.set_content(f"""
    Olá!

    Você solicitou a redefinição da sua senha.

     Aqui está o código para redefinir sua senha:
     {token}

    Este códiem 1 hora.go expira  Se você não solicitou isso, ignore este e-mail.

    Atenciosamente,
    0games7
    """)
    try:
        # Conectar ao servidor SMTP do Gmail
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_EMISSOR, SENHA)  # Autenticação
            smtp.send_message(msg)            # Enviar e-mail
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print("Erro ao enviar e-mail:", e)

enviar_email(destinatario="arthur.n.carvalho6@aluno.senai.br")
user_token = input("digite a o token: ")
if user_token == str(token):
    print("senha redifinida")
