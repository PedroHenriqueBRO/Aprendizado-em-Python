#calculadora

import os


def somar(a,b):
    return a+b
def dividir(a,b):
    if b==0:
        return
    return a/b
def multiplicar(a,b):
    return a*b
def subtrair(a,b):
    return a-b

def calculator():
        print("""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
              """
)
        a=int(input("qual o primeiro numero : "))
        b=int(input("qual o segundo numero : "))
        c=input("digite a operação : ")
        dicionario={
           "+":somar,
           "-":subtrair,
           "*":multiplicar,
           "/":dividir
        }
        result=dicionario[c]
        print(f"O resultado da operação foi : {result(a,b)}")
        d=result(a,b)
        continuar=input("Deseja continuar com o mesmo resultado em outras operações ? S/N ")
        while(continuar=="S"):
             b=int(input("qual o segundo numero : "))
             c=input("digite a operação : ")
             result=dicionario[c]
             print(f"O resultado da operação foi : {result(d,b)}")
             d=result(d,b)
             continuar=input("Deseja continuar com o mesmo resultado em outras operações ? S/N ")
        fechar=input("Deseja continuar a calcular ? : S/N ")
        if fechar=="S":
             os.system('cls')
             calculator()
        else:
             os.system('cls')
             return      
calculator()

    


    

