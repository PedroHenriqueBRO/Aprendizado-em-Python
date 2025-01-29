record=("Pedro","Henrique","(38)99309-3457","(21)99453-2103")
first_name,second_name,*numbers_phone=record
print(f"{first_name} {second_name} , {numbers_phone}")
record=("Pedro",50,123.45,(23,4,2002))
name,*_,(*_,year)=record
print(name)
print(year)
dados=[1,2,3,4,5,6,7,8,9,10]
first,*rest=dados
print(first)
print(rest)