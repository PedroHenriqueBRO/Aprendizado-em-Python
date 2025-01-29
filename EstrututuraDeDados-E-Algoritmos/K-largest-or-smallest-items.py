import heapq

dados=[1,2,3,4,5,6,29,392,34,6,78,2910,39284,1,0,20384,23983844,203,44]
print(heapq.nlargest(3,dados))#printa os 3 maiores elementos da lista dados
print(heapq.nsmallest(3,dados))#printa os 3 menores elementos da lista dados

portfolio=[{
'name':'tatu','idade':20
},{
    'name':'joao'
    ,'idade':15

},{
    'name':'maria'
    ,'idade':17

},{
    'name':'hiago'
    ,'idade':23

}]
print(heapq.nlargest(2,portfolio,key=lambda s:len(s['name'])))
