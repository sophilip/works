# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 13:13:02 2016

@author: Souhail
"""

from random import shuffle, randint

distance =  \
[[0, 440, 4749, 4959, 5038, 15669, 2807, 4542, 5381, 6737, 4364, 6297, 14014, 1872, 622],
 [440, 0, 4511, 4806, 4631, 15226, 2483, 4725, 5129, 6540, 4168, 5935, 13582, 1796, 880],
 [4749, 4511, 0, 1030, 5800, 12472, 5611, 9225, 628, 2095, 7553, 7366, 10073, 3031, 4422],
 [4959, 4806, 1030, 0, 6765, 12974, 6308, 9501, 1197, 1836, 8285, 8350, 10501, 3100, 4510],
 [5038, 4631, 5800, 6765, 0, 10731, 2466, 6351, 6059, 7487, 2906, 1611, 9780, 5519, 5480],
 [15669, 15226, 12472, 12974, 10731, 0, 13159, 14833, 11935, 11319, 12382, 9738, 2493, 15104, 15931],
 [2807, 2483, 5611, 6308, 2466, 13159, 0, 4386, 6107, 7671, 1982, 3508, 12199, 3935, 3361],
 [4542, 4725, 9225, 9501, 6351, 14833, 4386, 0, 9833, 11264, 3538, 6378, 15562, 6407, 5019,],
 [5381, 5129, 628, 1197, 6059, 11935, 6107, 9833, 0, 1564, 8015, 7576, 9506, 3657, 5049],
 [6737, 6540, 2095, 1836, 7487, 11319, 7671, 11264, 1564, 0, 9575, 8926, 8825, 4906, 6322],
 [4364, 4168, 7553, 8285, 2906, 12382, 1982, 3538, 8015, 9575, 0, 2895, 12214, 5820, 4980],
 [6297, 5935, 7366, 8350, 1611, 9738, 3508, 6378, 7576, 8926, 2895, 0, 9320, 7044, 6813],
 [14014, 13582, 10073, 10501, 9780, 2493, 12199, 15562, 9506, 8825, 12214, 9320, 0, 12916, 14043],
 [1872, 1796, 3031, 3100, 5519, 15104, 3935, 6407, 3657, 4906, 5820, 7044, 12916, 0, 1417],
 [622, 880, 4422, 4510, 5480, 15931, 3361, 5019, 5049, 6322, 4980, 6813, 14043, 1417, 0]]

class Individu:
    def __init__(self):
        """
        Individu défini sans attribut, on ajoute directement un code génétique
        """
        l = [0,1,2,3,4,5,6,7,8,9, 10, 11, 12, 13, 14]
        shuffle(l)
        self.gen = l
    
    def getgen(self):
        """
        Just a getter
        """
        return(self.gen)
        
    def setdistance(self):
        """
        Ajoute un attribut à l'individu, distance.
        """
        dist_calc = 0
        for i in range( len( self.gen ) -1 ):
            dist_calc += distance[ self.gen[ i ] ][ self.gen[ i+1 ] ]
        dist_calc += distance[ self.gen[ -1 ] ][ self.gen[ 0 ] ]
        self.distance = dist_calc
    
    def getdistance(self):
        """
        Just a getter. With a setter in case.
        """
        self.setdistance()
        return(self.distance)
        
    def cross_breeding(self, x, y):
        """
        Input : parents --> Individu() type
        Output : code gen croisé --> liste
        """
        k = randint(0, len(x)-1)
        child = x[:k]
        for i in y:
            if i not in child:
                child.append(i)
        self.gen = child
                
    def mutation(self):
        """
        Mutate deux éléments du code génétique aléatoire, mais pas les mêmes.
        """
        a, b = 0, 0
        while a == b:
            a = randint(0, len(self.getgen()) -1)
            b = randint(0, len(self.getgen()) -1)
        gen = self.getgen()
        memory = gen[a]
        gen[a] = gen[b]
        gen[b] = memory
        self.gen = gen
        
        
def run(nb_gen):
    
    pop = []
    for i in range(100):
        pop.append(Individu())
    new_gen = []
    """
    Creation de la population 0
    """
    for i in range(nb_gen):
        
        for i in range(200):
            x = pop[randint(0, len(pop)-1)].getgen()
            y = pop[randint(0, len(pop)-1)].getgen()
            child = Individu()
            child.cross_breeding(x,y)
            k = randint(0, 1)
            if k == 0:
                child.mutation()
            new_gen.append(child)
            """
            Creation de 200 enfants.
            Parents au hasard.
            1 chance sur 2 d'avoir une mutation
            """
        new_gen.sort(key=lambda x: x.getdistance(), reverse=False) 
        """
        Tri de notre generation avec en clef la distance, de façon croissante
        """
        pop = pop[:60]
        pop += new_gen[:40]
        shuffle(pop)
        """
        Creation de la population x + 1, avec 60 individu de la populatin X - 1 et 
        les 40 meilleurs de la gen X. 
        Shuffle pour ne pas avoir toujours les mêmes 60 d'avant.
        """
                
    meilleur = min(pop, key = lambda x: x.getdistance())
    print("Le meilleur chemin de cette simulation est :", meilleur.getgen(), "avec une distance de :", meilleur.getdistance())
    """
    Affichage du meilleur, trouve avec un min + distance en key.
    """
