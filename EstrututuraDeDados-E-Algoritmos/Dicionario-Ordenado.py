from collections import OrderedDict
d=OrderedDict()
d['foo']=1
d['bar']=2
d['spam']=3
d['grok']=4
for key in d:
    print(f"Key: {key} , value : {d[key]}")