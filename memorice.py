from numpy import random
N_pares = int(input("Insert amount of cards to play:"))+1

Cartas = []
for i in range(N_pares):
    Cartas.append(range(N_pares)[i])
    Cartas.append(range(N_pares)[i])

Cartas.pop(0)
Cartas.pop(0)
Cartas_totales = len(Cartas)
#print (Cartas)
Mezcla=[]
while len(Cartas) > 0:
    x=Cartas[random.randint(len(Cartas))]
    Mezcla.append(x)
    Cartas.remove(x)

#print (Mezcla)
print(Cartas_totales)
    
