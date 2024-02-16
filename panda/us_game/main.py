import turtle
import pandas
import os
d=pandas.read_csv("C:/Users/xtron/Desktop/python/panda/us_game/50_states.csv")#lê o arquivo csv

from turtle import Screen 

screen= Screen()#abre uma tela

c="C:/Users/xtron/Desktop/python/panda/us_game/blank_states_img.gif"

screen.addshape(c)
lista=d.state.to_list()

turtle.shape(c)#adiciona uma tartaruga com o shape da variável c, que no caso é a imagem do programa

acertos=[]

while len(acertos)<50:
    questao=screen.textinput(title=f"{len(acertos)}/50 : ",prompt="Estado : ")#cria a caixinha de perguntas na tela
    if questao=="exit":
        break
    elif questao in lista:
        acertos.append(questao)
        t=turtle.Turtle()#Cria uma tartaruga
        t.hideturtle()#esconde a forma de tartaruga
        t.penup()#impede ela de fazer desenhos
        estado=d[d.state==questao]
        t.goto(int(estado.x) , int(estado.y))
        t.write(estado.state.item())
erros=[

]

for estado in lista:
    if estado not in acertos:
        erros.append(estado)
newdata=pandas.DataFrame(erros)
print(newdata)
newdata.to_csv(os.path.join("C:/Users/xtron/Desktop/python/panda/us_game",r'green1.csv'))





