from random import shuffle,randrange
from math import sqrt, floor
class Genetique:

    def __init__(self,genes,nb_population) -> None:
        self.genes = genes
        self.population = self.generationPopulation(nb_population)
    
    def generationIndividu(self):
        individu = self.genes.copy()
        shuffle(individu)
        individu.insert(0,{0:[0,0]})
        return individu
    
    def generationPopulation(self,nb_population):
        return [self.generationIndividu() for i in range(nb_population)]
    
    def evaluationPopulation(self,population):
        list_population = population.copy()
        list_distance = []
        for item in population:
            distance = 0
            tempo = []
            for point in item:
                coord = []
                #print(point)
                for value in point.values():
                    coord = value
                    
                if len(tempo) > 0:
                    distance += sqrt((coord[0]-tempo[0])**2 + (coord[1]-tempo[1])**2)
                tempo = coord
            list_distance.append(distance)
        list_selection = []
        print(list_distance)
        for i in range(floor(len(list_distance)/3)):
            index_distance_minimum = list_distance.index(min(list_distance))
            list_selection.append(list_population.pop(index_distance_minimum))
            list_distance.pop(index_distance_minimum)
        return list_selection
    
    def croisement(self,population):
        enfants = []
        i = 0
        while i < len(self.population) - len(population):
            rand = i
            while rand == i:
                rand = randrange(len(population))
            parent1 = population[i % len(population)]
            parent2 = population[rand]
            enfant = parent1[0:randrange(1,len(parent1) - 2)]
            for item in parent2:
                if item in enfant:
                    pass
                else:
                    enfant.append(item)
            enfants.append(enfant)
            i += 1
        return population + enfants
    
    def mutation(self,population):
        population_mutante = []
        i = 0
        for individu in population:
            mutant = individu.copy()
            if i > 2:
                if(randrange(100) < 20):
                    index_1 = randrange(1,len(individu))
                    index_2 = index_1
                    while index_2 != index_1:
                        index_2 = randrange(1,len(individu))
                    mutant[index_1], mutant[index_2] = mutant[index_2], mutant[index_1]
            else:
                i += 1
            population_mutante.append(mutant)
        return population_mutante
    
    def chemin_plus_cours(self,nombre_iteration):
        population = self.population
        for i in range(nombre_iteration):
            population = self.evaluationPopulation(population)
            population = self.croisement(population)
            population = self.mutation(population)
        
        list_distance = []
        for item in population:
            distance = 0
            tempo = []
            for point in item:
                coord = []
                for value in point.values():
                    coord = value

                if len(tempo) > 0:
                    distance += sqrt((coord[0]-tempo[0])**2 + (coord[1]-tempo[1])**2)
                tempo = coord
            list_distance.append(distance)
        
        return population[list_distance.index(min(list_distance))], min(list_distance)