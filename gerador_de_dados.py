#importação de biblioetecas 
import random
import time
import os 
import sys 

def clear():
    #ver qual é o nome do sitma
    if sys.platform.startswith("win32"):
        #aqui é para o windwos
        return os.system("cls")
    else:
        #aqui é para o linux e macos
        return os.system("clear")
    
#parte em loop
def numero_aleatorio(lados:int):
    print('')#só para dar um espaço 
    #atribir um valor aleatori entre 1 á n° de lados que o dado tem a variavel n
    n = random.randrange(1, lados) 

    #informa para o usario qual foi o n° gerado
    print(f'O valor do dado é:  {n}')
    print("")
    
    #questona se o usario quer continuar com o programar
    input_user = input("vc que rodar o mesmo dado denovo? Responda com Y = sim e N = não: ")

    #caso a reposda seja n(não) então o programa ira pergunta se que ser finlizado 
    if input_user == 'n' or  input_user == 'N':
        input_user2 = input("vc deseja sair? Y = sim e N = não: ")
        #se a resposda for sim o programa ira fecha é entregar uma utima mesagem ao usuario
        if input_user2 == 'y' or input_user2 == 'Y':
            print('ok tachu')
        #caso se seja não o programa vai pergunta se quere-se inserir outro valor no dado
        elif input_user2 == 'n' or input_user2 == 'N':
            numeroslados = input('insira o numeros de lados do dado que seja maior que ou igual á 2: ')
            #tratamento de erro para garantir q a linha 10  não de erro
            if numeroslados.isdigit():
                lados = int(numeroslados)
                if lados != 1 and lados != 0:
                    numero_aleatorio(lados)
                else:
                    erro_resposda()
            else:
                erro_resposda()
        else:
            erro_resposda()

    #caso ele seja y(sim) então o programa entrar em loop
    elif input_user == 'y' or input_user == 'Y':
        #limpar o terminal
        time.sleep(3)#3secondsc
        clear()
        numero_aleatorio(lados)
        pass

    #caso não seja inserido n/y o programa ira interpleta como sim além de dar um saida de erro para o usario
    else: 
        erro_resposda()    

#complemento de tramaento de erro
def erro_resposda():
    print('caracterico incorreto')
    print('o dado dera 6 lados')
    time.sleep(5)#seconds
    os.system('cls')
    numero_aleatorio(6)


#uma introdução do programa
print('seja bem vindo ao gerado de dados')
Lados = input('insira o numeros de lados do dado que seja maior que ou igual á 2: ') 

#verifica foi digitado só n° >= 2
if Lados.isdigit():
    #conversão de var texto para var n°
    #isso se deve para que não ajar bugs na linha 10
    NLados = int(Lados)

    if NLados != 1 and NLados != 0:
        #chama a função 
        numero_aleatorio(NLados)
    else:
        #chamada da bloco complementar do tratamento de erro
        erro_resposda()
else:
    erro_resposda()