import pandas
#mostra o arquivo em forma de tabela
dados=pandas.read_csv("C:/Users/xtron/Desktop/python/panda/weather_data.csv")
print(dados)
#csv para dicionario
dict=dados.to_dict()
print(dict)
#csv para lista
list=dados["temp"].to_list()
print(list)
media=0
for temps in list:
    media=temps+media
print(f"temperatura media = {round(media/len(list),2)}")

#a media dos valores da série
print(round(dados["temp"].mean(),2))
#o maximo dos valores contido na série
print(dados["temp"].max())
#consulta nas coluna dada qual linha possui a especificação e se houver ele retorna a linha inteira
print(dados[dados.day=="Monday"].temp)

#criar um frame de dados a partir de um dicionario

dicionario={
    "nomes":["Pedro","joao","ana"],
    "scores":[0,2,4]
}
novo=pandas.DataFrame(dicionario)
print(novo)
novo.to_csv("new_csvfile")