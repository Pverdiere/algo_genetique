from genetique import Genetique
from random import randrange,seed
from math import sqrt

seed(42)

points = []

for i in range(1,41):
    points.append({i:[randrange(10000),randrange(10000)]})

#print(points)

genetique = Genetique(points,50)

print("final",genetique.chemin_plus_cours(50))