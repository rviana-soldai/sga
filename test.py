#from Coin import Coin
from Individual import Individual

i = Individual(7)
j = Individual(7)

print(i.print())
print(j.print())
for it in range(7):
	i.setBit(it, True)
	j.setBit(it, False)

print(i.print())
print(j.print())

sons = i.cross(2, j)
print(sons[0].print())
print(sons[1].print())