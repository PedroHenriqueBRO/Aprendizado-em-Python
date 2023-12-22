import random as r
import stages
import palavras as words

palavra = words.palavras[r.randint(0, 7)]
print("------ JOGO DA FORCA ------")
i = 0
print("A palavra a ser adivinhada é a seguinte : ")
palavraatualizada = []
while i < len(palavra):
    print("_ ", end="")
    palavraatualizada.append("_ ")
    i += 1
print("")
print(
    """
      |------|
      o      |
     /|\     |
     / \     |
     ---------
"""
)
print("")
vida = 6
letrasfaltando = len(palavra)
errou = False
cont = 0
while True:
    if vida == 0:
        print("Voce perdeu!!!")
        break
    elif vida != 0 and letrasfaltando == 0:
        print("Voce ganhou!!!")
        break
    print("Digite uma letra : ")
    letra = input()
    print("Palavra atualizada")
    for n in range(0, len(palavra)):
        if palavra[n] == letra:
            palavraatualizada[n] = letra
            print(palavraatualizada[n] + " ", end="")
            letrasfaltando -= 1
            cont -= 1
        else:
            print(palavraatualizada[n] + " ", end="")
    print("")

    if cont == 0:
        errou = True
    cont = 0
    if errou:
        vida -= 1
        errou = False
    stages.verificavida(vida)
