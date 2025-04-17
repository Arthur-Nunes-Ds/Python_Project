#info:
    #liguagems: python
    #Feito por: Arthur Nunes de Carvalho
    #objetivo: gerar uma tabela no terminal como nome do aluno nota dos 4 bimestre a média é verificar qual statos o aluno estár
    #titulo: media
#importações de bibliotcas
from os import system as comand
from time import sleep as delay
import pandas as pd
import sys
#essa ista tem que ficar aqui para não ser zeradas no porcausa do loop do 'while true'      
nome_d_aluno = []
nome_aluno_a = []
bi1_a =[]
bi2_a =[]
bi3_a =[]
bi4_a =[]
media_a = []
pasado_str_a = []
#limpar o terminal
def clear():
     #verifia se o sitema é winddwos
     if sys.platform.startswith('win32'):
     #caso seja ele rota cls no termenial do user
          #delay basico para não limpara a tela automaticamente
          delay(1.2)
          return comand('cls')
     else:
     #caso não seja ele rota clear no termenial do user
          delay(1.2)
          return comand('clear')
     #deve ser usado o *return* para que execute essa parte é volte da linha seguinte á qual foi chamada
#repetir para sempre {o while repede até que determinada condisão se torna Falsa; 
#nesse caso ele não sovre alteração é já que ele receber True direto, assim executando o bloco dentro dele para sempre}
while True:
    #inputs para o usauario:
    nome_aluno = input("Insira o nome do aluno: ")#pede o nome do aluno atribui a nome_aluno
    bi1 = input("Insira a nota do 1° bimestre: ")#pedea nota do 1°bi aluno atribui BI1
    bi2 = input("Insira a nota do 2° bimestre: ")#pedea nota do 2°bi aluno atribui BI2
    bi3 = input("Insira a nota do 3° bimestre: ")#pedea nota do 3°bi aluno atribui BI3
    bi4 = input("Insira a nota do 4° bimestre: ")#pedea nota do 4°bi aluno atribui BI4
    media = 0 #media inicial 
    pasado_str = "" #situação final incialmente não tem
    pasado = False #inicalmente o auluno não esta pasado
    #add valor de nome_d_aluno ná lista de nome_aluno[]
    nome_d_aluno.append(nome_aluno)
    #verificar se o que foi digitado pelo usuario é um n°{nesse caso ele só vai ser verdardeiro se ás 4 var de bimestre for digito}
    if bi1.isdigit() == True and bi2.isdigit() == True and bi3.isdigit() == True and bi4.isdigit() == True:
          #conversor de str(caracter) --> int(n° sem virgula)
          Bi1 = int(bi1);Bi2 = int(bi2);Bi3 = int(bi3);Bi4 = int(bi4)
          #verifica se os bimestres estão entre 0 á 100 e executar só se todos estiveren dentro desse intervalor e que não seja negativo/decimal(n° com ',')
          if((Bi1>=0 and Bi1<=100)and(Bi1!=float))and((Bi2>=0 and Bi2<=100)and(Bi2!=float))and((Bi3>=0 and Bi3<=100)and(Bi3!=float))and((Bi4>=0 and Bi4<=100)and(Bi4!=float)):
               bi1_a.append(bi1)
               bi2_a.append(bi2)
               bi3_a.append(bi3)
               bi4_a.append(bi4)
               media = (Bi1+Bi2+Bi3+Bi4)/4
          else:
               bi1_a.append(0)
               bi2_a.append(0)
               bi3_a.append(0)
               bi4_a.append(0)
               print("erro")
               media = 50
     #caso ao contario ele avisa ao user q ove algum erro ná hora de digitar a nota
    else:
         bi1_a.append(str("null"))
         bi2_a.append(str("null"))
         bi3_a.append(str("null"))
         bi4_a.append(str("null"))
         print("erro")
     #verificador se o aluno passou ou não
    if media >= 70:
         pasado_str = "aprovado"
    elif media <= 35:
         pasado_str = "reprovado"
    else:
         pasado_str = "recuperação"
     #add valor de media_a ná lista de media[]
     #add valor de pasado_str ná lista de pasado_str_a[]
    media_a.append(media)
    pasado_str_a.append(pasado_str)
    #sistema de tempo/limpar a tela
    clear()
     #pergunta se o user finalizou de digitar os valores
    user_finish = input(" Insira s = sim e n = não \n Você terminou de inserir os dados da turma: ")
     #tabela               #coluna   #linha
    tabela = pd.DataFrame({'aluno:': nome_d_aluno,
                           'bi1:': bi1_a,
                           'bi2:': bi2_a,
                           'bi3:': bi3_a,
                           'bi4:': bi4_a,
                           'media final:': media_a,
                           'estado final:': pasado_str_a})
     #se o user terminou de editar a tabela, o código sera finaizado e inpreso a tabela mas uma de enseramento
    if user_finish.upper() == "S":
         print(f'Tabela final: \n {tabela}')
         print("OK tenha um bom dia \n ☆*: .｡. o(≧▽≦)o .｡.:*☆")
         break
    #casso acontario o código repitirar tudo denovo até que o user tenha terminado de digitado a tabela
    print(tabela)
    clear()