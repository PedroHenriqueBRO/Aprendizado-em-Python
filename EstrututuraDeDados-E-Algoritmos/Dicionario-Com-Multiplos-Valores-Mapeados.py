from collections import defaultdict
d={}
d.setdefault('a',[]).append(3)
d.setdefault('b',[]).append(4)
d.setdefault('c',[]).append(5)
d['a'].append(4)
print(d)
