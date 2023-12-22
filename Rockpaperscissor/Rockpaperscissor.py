import random as r

print("Escolha entre pedra,papel e tesoura")
escolha = input()
if escolha == "pedra":
    print("Sua escolha foi:")
    print(
        """
                    _    
                   | |   
     _ __ ___   ___| | __
     | '__/ _ \ / __| |/ /
     | | | (_) | (__|   < 
     |_|  \___/ \___|_|\_/
    """
    )
elif escolha == "papel":
    print("Sua escolha foi:")
    print(
        """
     _ __   __ _ _ __   ___ _ __ 
    | '_ \ / _` | '_ \ / _ \ '__|
    | |_) | (_| | |_) |  __/ |   
    | .__/ \__,_| .__/ \___|_|   
    | |         | |              
    |_|         |_|      
     """
    )
elif escolha == "tesoura":
    print("Sua escolha foi:")
    print(
        """
     _       ,/'
    (_).  ,/'
     __  ::
    (__)'  `\.
            `\.
     """
    )
aleatorio = r.randint(0, 2)
if aleatorio == 0:
    print("Sua escolha foi:")
    print(
        """
                    _    
                   | |   
     _ __ ___   ___| | __
     | '__/ _ \ / __| |/ /
     | | | (_) | (__|   < 
     |_|  \___/ \___|_|\_/
    """
    )
    if escolha == "papel":
        print("Voce ganhou")
    elif escolha == "tesoura":
        print("Voce perdeu")
    else:
        print("Indefinido")
elif aleatorio == 1:
    print("Sua escolha foi:")
    print(
        """
     _ __   __ _ _ __   ___ _ __ 
    | '_ \ / _` | '_ \ / _ \ '__|
    | |_) | (_| | |_) |  __/ |   
    | .__/ \__,_| .__/ \___|_|   
    | |         | |              
    |_|         |_|      
     """
    )
    if escolha == "pedra":
        print("Voce perdeu")
    elif escolha == "tesoura":
        print("Voce ganhou")
    else:
        print("Indefinido")
elif aleatorio == 2:
    print("Sua escolha foi:")
    print(
        """
     _       ,/'
    (_).  ,/'
     __  ::
    (__)'  `\.
            `\.
     """
    )
    if escolha == "papel":
        print("Voce perdeu")
    elif escolha == "pedra":
        print("Voce ganhou")
    else:
        print("Indefinido")
