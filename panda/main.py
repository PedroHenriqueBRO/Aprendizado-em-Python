import csv

dados=[]
with open("C:/Users/xtron/Desktop/python/panda/weather_data.csv") as data:
    texto=data.readlines()
    for datas in texto:
        dados.append(datas.strip())
dados.pop(0)
print(dados)
print("")
with open("C:/Users/xtron/Desktop/python/panda/weather_data.csv") as data:
    rows=csv.reader(data)
    temperaturas=[]
    for row in rows:
        temperaturas.append(row[1])
        print(row)
temperaturas.pop(0)
print(temperaturas)

