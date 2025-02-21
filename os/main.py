#importação de biblioetecas 
import random
import time
import os 

#uma introdução do programa
print('seja bem vindo ao gerado de dados')

#um tempinho para não ir tudo instanio 
time.sleep(2)#2seconds

#parte em loop
while True:
    print('')#só para dar um espaço 
    #atribir um valor aleatori entre 1 á 6 a variavel n
    n = random.randrange(1, 6) 

    #informa para o usario qual foi o n° gerado
    print(f'O valor do dado é:  {n}')
    print("")
#blablbalbalablabalab
    #questona se o usario quer continuar com o programar
    input_user = input("vc que rodar o dado denovo? Responda com Y = sim e N = não.")

    #caso a reposda seja n(não) então sera finlizado o programa
    if input_user == 'n' or  input_user == 'N':
        print('ok até mais')
        break  

    #caso ele seja y(sim) então o programa entrar em loop
    elif input_user == 'y' or input_user == 'Y':
        #limpar o terminal
        os.system("cls")
        time.sleep(3)#3secondsc
        pass

    #caso não seja inserido n/y o programa ira interpleta como sim além de dar um saida de erro para o usario
    else: 
        print('caracterio invalido')
        print('o programa dara outro n° a você.')
        time.sleep(3)#3seconds
        