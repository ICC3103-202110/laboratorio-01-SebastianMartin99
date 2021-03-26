from numpy import random
N_pairs = int(input("Insert amount of playing cards you want to play:"))+1

Cards = []
for i in range(N_pairs):
    Cards.append(range(N_pairs)[i])
    Cards.append(range(N_pairs)[i])

Cards.pop(0)
Cards.pop(0)
Shuffle=[]
while len(Cards) > 0:
    x=Cards[random.randint(len(Cards))]
    Shuffle.append(x)
    Cards.remove(x)

#print (Shuffle)
Board=[]
for i in range(len(Shuffle)):
    Board.append(0)

print (Board)
First_P_Card = int(input("Select position of one playing card:"))
Board.pop(First_P_Card)
Board.insert(First_P_Card-1,Shuffle[First_P_Card-1])

print(Board)

Second_P_Card = int(input("Select the second one:"))
Board.pop(Second_P_Card)
Board.insert(Second_P_Card-1,Shuffle[Second_P_Card-1])
print (Board)
if Shuffle[First_P_Card-1] == Shuffle[Second_P_Card-1]:
    print ("Correct")
    
else:
    print ("Wrong one")
    Board=[]
    for i in range(len(Shuffle)):
        Board.append(0)
    print (Board)





    


