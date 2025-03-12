#info:
    #liguagems: python
    #Feito por: Arthur Nunes de Carvalho
    #objetivo: pega um n° do user é ver ser ele é impar ou par
    #titulo: impar ou par
#bibliotecas:
import os
from time import sleep as time
import sys 

#comando para limpar o terminal todo
def clear():
    #pega o nome do sitema
    #ver qual é o nome do sitma
    if sys.platform.startswith("win32"):
        #aqui é para o windwos
        return os.system("cls")
    else:
        #aqui é para o linux e macos
        return os.system("clear")

#para o codigo entrar em loop
while True:
    #input do user
    print("========================================")
    input_user = input('caso desja sair digite "exit" ou "quit"\n"insira um numero inteiro:')
    print("========================================")
    #comando para sair do sitema(exit/quit)
    #str'.lower()'== deixa tudo dendro da str em minisculo
    if input_user.lower() == "exit" or input_user.lower == "quit":
        #time de 1.5 s
        time(1.5)
        #limpar a tela
        clear()
        #finaliza o o código
        print("==================================")
        print("ok, até\n☆*: .｡. o(≧▽≦)o .｡.:*☆")
        print("==================================")
        break
    #verefica se foi digitado um numero inteiro
    elif input_user.isdigit():
        #verefica se tem resto na divissão n°/2 
        if int(input_user)%2 == 0:
            time(1.5)
            clear()
            #fala quer é par
            print("====")
            print("par")
            print("====")
        else:
            time(1.5)
            clear()
            print("=====")
            #fala q é impar
            print("impar")
            print("=====")
    #tratamento de erro
    else:
        time(1.5)
        clear()
        #quase xingar o user de burro
        print("============================")
        print("SÓ DIGITE NUMEROS INTEIROS!!")
        print("============================")
    time(1.5)
    clear()