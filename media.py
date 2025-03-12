from os import system as comand
from time import sleep as delay
import pandas as pd
import sys

nome_d_aluno = []
nome_aluno_a = []
bi1_a =[]
bi2_a =[]
bi3_a =[]
bi4_a =[]
media_a = []
pasado_str_a = []

def clear():
     if sys.platform.startswith('win32'):
          return comand('cls')
     else:
          return comand('clear')

while True:
    nome_aluno = input("Insira o nome do aluno: ")
    bi1 = input("Insira a nota do 1° bimestre: ")
    bi2 = input("Insira a nota do 2° bimestre: ")
    bi3 = input("Insira a nota do 3° bimestre: ")
    bi4 = input("Insira a nota do 4° bimestre: ")
    media = 0
    pasado_str = ""
    pasado = False
    
    nome_d_aluno.append(nome_aluno)

    if bi1.isdigit() == True and bi2.isdigit() == True and bi3.isdigit() == True and bi4.isdigit() == True:
         Bi1 = int(bi1)
         Bi2 = int(bi2)
         Bi3 = int(bi3)
         Bi4 = int(bi4)
         media = (Bi1+Bi2+Bi3+Bi4)/4
         bi1_a.append(bi1)
         bi2_a.append(bi2)
         bi3_a.append(bi3)
         bi4_a.append(bi4)
    else:
         bi1_a.append(0)
         bi2_a.append(0)
         bi3_a.append(0)
         bi4_a.append(0)
         print("erro")
   
    if media >= 70:
         pasado = True
         pasado_str = "aprovado"
    else:
         pasado_str = "reprovado"

    media_a.append(media)
    pasado_str_a.append(pasado_str)

    delay(1.2)
    clear

    user_finish = input(" Insira s = sim e n = não \n Você terminou de inserir os dados da turma: ")

    tabela = pd.DataFrame({'aluno:': nome_d_aluno,
                           'bi1:': bi1_a,
                           'bi2:': bi2_a,
                           'bi3:': bi3_a,
                           'bi4:': bi4_a,
                           'media final:': media_a,
                           'estado final:': pasado_str_a})

    if user_finish.upper() != "S":
         print(f'Tabela final: \n {tabela}')
         print("OK tenha um bom dia \n ☆*: .｡. o(≧▽≦)o .｡.:*☆")
         break
    
    print(tabela)
    delay(1.2)
    clear