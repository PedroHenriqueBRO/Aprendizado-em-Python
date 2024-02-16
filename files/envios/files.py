mudar="[name]"

with open("C:/Users/xtron/Desktop/python/files/carta/modelo.txt") as modelo:
    texto=modelo.read()
    d=open("C:/Users/xtron/Desktop/python/files/invitednames/nomes.txt")
    nome=d.readlines()
    for nomes in nome:
     novotexto=texto.replace("[name]",nomes.strip())
     print(novotexto)
     with open(f"C:/Users/xtron/Desktop/python/files/envios/nova_carta_para_{nomes.strip()}.txt","w") as new:
        new.write(novotexto)





        


    
