import heapq
class PriorityQueue:
    def __init__(self):
        self.queue=[]
        self.index=0
    def push(self,item,priority):
        heapq.heappush(self.queue,(-priority,item,self.index))#mantem heap de minimo logo é preferivel usar -priority para colocar os de maior prioridade no topo do heap
        self.index+=1
    def pop(self):
        heapq.heappop(self.queue)[-1]
    
class Item:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return "Item({!r})".format(self.name)
q=PriorityQueue()
q.push(Item("Caixa"),2)
q.push(Item("Faca"),3)
q.push(Item("Celular"),4)
q.push(Item("Mala"),5)
for item in q.queue:
    print(item)
