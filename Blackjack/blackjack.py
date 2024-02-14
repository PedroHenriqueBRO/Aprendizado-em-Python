import os
import random


cartas=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def entregar():
    c=random.randint(0,12)
    return cartas[c]
def usuinicial():
    cartasus=[]
    soma=0
    for i in range(2):
        cartasus.append(entregar())
        if soma==22:
            cartasus.remove(11)
            cartasus.append(1)
    return cartasus
    
def compinicial():
    soma=0
    cartascomp=[]
    for i in range(2):
        cartascomp.append(entregar())
        if soma==22:
            cartascomp.remove(11)
            cartascomp.append(1)
    return cartascomp
def score(conjunto):
    soma=0
    for i in conjunto:
        soma=soma+i
    return soma
def compare(usscore,compscore):
    if usscore>21:
        print("A casa ganhou!!!")
    elif compscore>21:
        print("Usuário ganhou!!!")
    elif usscore>compscore:
        print("Usuário ganhou!!!")
    elif usscore==21:
        print("Usuário ganhou!!!")
    elif compscore>usscore:
        print("A casa ganhou!!!")
    elif usscore==compscore:
        print("É um empate!!!")

def blackjack():

    cartasus=[]
    usscore=0   
    cartascomp=[]
    compscore=0
    print("""
  _ _ _ _ ___ ___ _ _ _ ___ _ _ _________
 |A|Q|1|5|4  |7  |J|1|9|7  |A|K|2        |
 |@|@|@|@|@  |## |O|O|O|OO |+|+|+        |
 | | | | | @ |   | | | |   | | |    +    |
 | | | | |   | # | | | | O | | |         |
 | | | | | @ |   | | | |   | | |    +    |
 | | | | |   | # | | | | O | | |        +|
 | | | | |   |   | | | |   | | |        Z|
  ~ ~ ~ ~ ~~~ ~~~ ~ ~ ~ ~~~ ~ ~ ~~~~~~~~~
          """)
    cartasus=usuinicial()
    usscore=score(cartasus)
    if usscore==21:
        print(f"As cartas do computador são : [{cartascomp}]")
        print(f"As cartas do usuario são : [{cartasus}]")
        print("Usuario ganhou!!!")
        p=input("Deseja jogar novamente ? : S/N ")
        if p=="S":
            os.system('cls')
            blackjack()
        return
    cartascomp=compinicial()
    compscore=score(cartascomp)

    print(f"Suas cartas iniciais são : {cartasus}")
    print(f"A primeira carta inicial do computador é : [{cartascomp[0]}]")

    c="S"
    while(c=="S"):
         c=input("Deseja pegar mais cartas ? : S/N ")
         if c=="S":
            d=entregar()
 
            if d==11 and usscore+d>21:
                d=1
                cartasus.append(1)
                usscore=score(cartasus)
                print(f"As cartas do usuario são : [{cartasus}]")
                print("--------------------------------------")
                if usscore>21:
                    print(f"As cartas do computador são : [{cartascomp}]")
                    print(f"As cartas do usuario são : [{cartasus}]")
                    print("A casa ganhou!!!")
                    p=input("Deseja jogar novamente ? : S/N ")
                    if p=="S":
                       os.system('cls')
                       blackjack()
                    return
                continue
            elif usscore+d==21:
                cartasus.append(d)
                usscore=score(cartasus)
                print(f"As cartas do computador são : [{cartascomp}]")
                print(f"As cartas do usuario são : [{cartasus}]")
                print("Usuário ganhou!!!")
                p=input("Deseja jogar novamente ? : S/N ")
                if p=="S":
                   os.system('cls')
                   blackjack()
                return
            else:
                cartasus.append(d)
                usscore=score(cartasus)
                print(f"As cartas do usuario são : [{cartasus}]")
                print("--------------------------------------")
                if usscore>21:
                    print(f"As cartas do computador são : [{cartascomp}]")
                    print(f"As cartas do usuario são : [{cartasus}]")
                    print("A casa ganhou!!!")
                    p=input("Deseja jogar novamente ? : S/N ")
                    if p=="S":
                       os.system('cls')
                       blackjack()
                    return
         else:
             c="N"
    while(compscore<17):
        d=entregar()
        if d+compscore>21 and d==11:
            d=1
            cartascomp.append(d)
            compscore=score(cartascomp)
            if compscore==21:
                print(f"As cartas do computador são : [{cartascomp}]")
                print(f"As cartas do usuario são : [{cartasus}]")
                print("A casa ganhou!!!")
                return
            elif compscore>21:
                print("Usuario ganhou!!!")
                p=input("Deseja jogar novamente ? : S/N ")
                if p=="S":
                   os.system('cls')
                   blackjack()
                return
        else:
            cartascomp.append(d)
            compscore=score(cartascomp)
            if compscore>21:
                print(f"As cartas do computador são : [{cartascomp}]")
                print(f"As cartas do usuario são : [{cartasus}]")
                print("Usuario ganhou!!!")
                p=input("Deseja jogar novamente ? : S/N ")
                if p=="S":
                   os.system('cls')
                   blackjack()
                return
    print("--------------------------------------")
    print(f"As cartas do computador são : [{cartascomp}]")
    print(f"As cartas do usuario são : [{cartasus}]")
    compare(usscore,compscore)
    p=input("Deseja jogar novamente ? : S/N ")
    if p=="S":
        os.system('cls')
        blackjack()
    

blackjack()
