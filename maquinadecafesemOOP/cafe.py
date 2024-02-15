MENU = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def inserirmoedas(total):
    print("Aceitamos moedas de 25,50 e 1 real")
    a = int(input("Quantas moedas de 25 centavos voçê irá inserir ? : "))
    b = int(input("Quantas moedas de 50 centavos voçê irá inserir ? : "))
    c = int(input("Quantas moedas de 1 real voçê irá inserir ? : "))
    total += a * 0.25 + b * 0.5 + c * 1
    return total


def report():
    print(f"Recursos restantes :{resources}")


def pedido(nome):
    custo = inserirmoedas(0)
    while custo < MENU[nome]["cost"]:
        print("Insira mais moedas")
        custo = inserirmoedas(custo)

    if nome != "espresso":

        resources["water"] = resources["water"] - MENU[nome]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[nome]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[nome]["ingredients"]["coffee"]
        if resources["water"] < 0 or resources["milk"] < 0 or resources["coffee"] < 0:
            print("Sem recursos suficientes")
        else:
            print("Pedido realizado")
    else:

        resources["water"] = resources["water"] - MENU[nome]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[nome]["ingredients"]["coffee"]
        if resources["water"] < 0 or resources["coffee"] < 0:
            print("Sem recursos suficientes")
        else:
            print("Pedido realizado")
        return


def maquina():
    requisicao = input("Qual o seu pedido ? : (espresso,latte ou cappucino) ou report ")

    if requisicao == "report":
        report()

    else:

        print("Insira moedas")
        pedido(requisicao)

    continua = input("Deseja pedir mais algo ? : S/N")

    if continua == "S":
        maquina()
    else:
        return


maquina()
