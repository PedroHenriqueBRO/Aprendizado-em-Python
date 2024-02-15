class CoffeeMachine():

    def __init__(self):
        self.total=0
        self.water=200
        self.milk=200
        self.coffee=100
        self.MENU = {
           "espresso": {     
               "ingredients": {
               "water": 50,
               "coffee": 18,
            },
               "cost": 1.5,
            },
            "latte": {
               "ingredients": {
               "water": 200,
               "milk": 150,
               "coffee": 24,
            },
               "cost": 2.5,
            },
            "cappuccino": {
               "ingredients": {
               "water": 250,
               "milk": 100,
               "coffee": 24,
            },
               "cost": 3.0,
            }
        }
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def inserirmoedas(self):   
        print("Aceitamos moedas de 25,50 e 1 real!!!")
        a = int(input("Quantas moedas de 25 centavos voçê irá inserir ? : "))
        b = int(input("Quantas moedas de 50 centavos voçê irá inserir ? : "))
        c = int(input("Quantas moedas de 1 real voçê irá inserir ? : "))
        self.total += a * 0.25 + b * 0.5 + c * 1

    def report(self):
        print(f"Recursos restantes :{self.resources} !!!")
    
    def pedido(self,nome):
        
        self.inserirmoedas()
        while self.total < self.MENU[nome]["cost"]:
            print("Insira mais moedas : ")
            self.inserirmoedas()

        if nome != "espresso":
            self.resources["water"] = self.resources["water"] - self.MENU[nome]["ingredients"]["water"]
            self.resources["milk"] = self.resources["milk"] - self.MENU[nome]["ingredients"]["milk"]
            self.resources["coffee"] = self.resources["coffee"] - self.MENU[nome]["ingredients"]["coffee"]
            if self.resources["water"] < 0 or self.resources["milk"] < 0 or self.resources["coffee"] < 0:
                print("Sem recursos suficientes!!!")
            else:
                print("Pedido realizado!!!")
        else:
            self.resources["water"] = self.resources["water"] - self.MENU[nome]["ingredients"]["water"]
            self.resources["coffee"] = self.resources["coffee"] - self.MENU[nome]["ingredients"]["coffee"]
            if self.resources["water"] < 0 or self.resources["coffee"] < 0:
                print("Sem recursos suficientes!!!")
            else:
                print("Pedido realizado!!!")
            return 
    def naosei(self):
        requisicao = input("Qual o seu pedido ? : (espresso,latte ou cappuccino) ou report ")
        if requisicao == "report":
            self.report()
        else:
            print("Insira moedas : ")
            self.pedido(requisicao)
        continua = input("Deseja pedir mais algo ? : S/N ")
        if continua == "S":
            self.naosei()
        else:
            return
        
    
    
        

        