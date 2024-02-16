import pandas 
d=pandas.read_csv("C:/Users/xtron/Desktop/python/panda/squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240216.csv")
list=[
]
list.append(("Gray",len(d[d["Primary Fur Color"]=="Gray"])))
list.append(("Black",len(d[d["Primary Fur Color"]=="Black"])))
list.append(("Cinnamon",len(d[d["Primary Fur Color"]=="Cinnamon"])))
print(list)
h=pandas.DataFrame(list)
print(h)



    

 


