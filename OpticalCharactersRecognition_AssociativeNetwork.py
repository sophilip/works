# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 01:25:45 2016

@author: Souhail
"""

point = "#"

N = 5 # nombre de lignes (et de colonnes) d'une forme/lettre

N_cell = N*N

# etats des cellules du reseau (booleens)
etats = [ False for _ in range(N_cell) ]


# seuils des cellules du reseau (reels)
seuils = [ 0.0 for _ in range(N_cell) ]

# poids des connexions du reseau (reels)
poids = [ [ 0.5 for _ in range(N_cell)] for _ in range(N_cell) ]

exemple_a_reconnaitre = [ [True,  False, True,  False, True],
                          [True,  True,  False, False, True],
                          [False, False, True,  False, True],
                          [True,  False, False, True,  True],
                          [True, False, False, False, True] ]

alphabet = \
[ [ [False, True,  True,  True,  False],  # { A }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  True],
     [True,  False, False, False, True],
     [True,  False, False, False, True] ],
   [ [True,  True,  True,  True,  False],  # { B }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False],
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False] ],
   [ [False, True,  True,  True,  True],   # { C }
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [False, True,  True,  True,  True] ],
   [ [True,  True,  True,  True,  False],  # { D }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False] ],
   [ [True,  True,  True,  True,  True],   # { E }
     [True,  False, False, False, False],
     [True,  True,  True,  False, False],
     [True,  False, False, False, False],
     [True,  True,  True,  True,  True] ],
   [ [True,  True,  True,  True,  True],   # { F }
     [True,  False, False, False, False],
     [True,  True,  True,  False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, False] ],
   [ [True,  True,  True,  True,  True],   # { G }
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, True],
     [True,  True,  True,  True,  True] ],
   [ [True,  False, False, False, True],   # { H }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  True],
     [True,  False, False, False, True],
     [True,  False, False, False, True] ],
   [ [False, False, True,  False, False],  # { I }
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False] ],
   [ [False, False, True,  True,  True],   # { J }
     [False, False, False, True,  False],
     [False, False, False, True,  False],
     [False, False, False, True,  False],
     [True,  True,  True,  True,  False] ],
   [ [True,  False, False, False, True],   # { K }
     [True,  False, False, True,  False],
     [True,  True,  True,  False, False],
     [True,  False, False, True,  False],
     [True,  False, False, False, True] ],
   [ [True,  False, False, False, False],  # { L }
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  True,  True,  True,  True] ],
   [ [True,  True,  False, True,  True],   # { N }
     [True,  False, True,  False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True] ],
   [ [True,  False, False, False, True],   # { M }
     [True,  True,  False, False, True],
     [True,  False, True,  False, True],
     [True,  False, False, True,  True],
     [True,  False, False, False, True] ],
   [ [False, True,  True,  True,  False],  # { O }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [False, True,  True,  True,  False] ],
   [ [True,  True,  True,  True,  False],  # { P }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False],
     [True,  False, False, False, False],
     [True,  False, False, False, False] ],
   [ [True,  True,  True,  True,  True],   # { Q }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, True,  True],
     [True,  True,  True,  True,  True] ],
   [ [True,  True,  True,  True,  False],  # { R }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False],
     [True,  False, False, True,  False],
     [True,  False, False, False, True] ],
   [ [False, True,  True,  True,  True],   # { S }
     [True,  False, False, False, False],
     [False, True,  True,  True,  False],
     [False, False, False, False, True],
     [True,  True,  True,  True,  False] ],
   [ [True,  True,  True,  True,  True],   # { T }
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False] ],
   [ [True,  False, False, False, True],   # { U }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [False, True,  True,  True,  False] ],
   [ [True,  False, False, False, True],   # { V }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [False, True,  False, True,  False],
     [False, False, True,  False, False] ],
   [ [True,  False, False, False, True],   # { W }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, True,  False, True],
     [False, True,  False, True,  False] ],
   [ [True,  False, False, False, True],   # { X }
     [False, True,  False, True,  False],
     [False, False, True,  False, False],
     [False, True,  False, True,  False],
     [True,  False, False, False, True] ],
   [ [True,  False, False, False, True],   # { Y }
     [False, True,  False, True,  False],
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False] ],
   [ [True,  True,  True,  True,  True],   # { Z }
     [False, False, False, True,  False],
     [False, False, True,  False, False],
     [False, True,  False, False, False],
     [True,  True,  True,  True,  True] ] ]




def affiche_forme (forme) :
    
    compteur = 0
    while compteur < 25 :
        for j in range(N):
            if forme[compteur] :
                print (point, end = "")
            else :
                print (" ", end = "")
            compteur = compteur + 1
        print()

# fonctions a completer --------------------------------------------

def initialise_reseau () :
    global poids, seuils, etats
    
    """Initialiser le réseau à un état neutre"""
    poids = [ [ 0.5 for _ in range(N_cell)] for _ in range(N_cell) ] 
    seuils = [ 0.0 for _ in range(N_cell) ]
    etats = [ False for _ in range(N_cell) ]
#    print("Réseau initialisé: valeur des poids: ", poids, "Valeur des seuils: ", seuils)
    """Rendre nulle la connexion de chaque cellule avec elle même"""    
    c = -1
    for i in range(N):
        for j in range(N):
            c += 1
            poids[c][c] = 0
    return
    
def presente_exemple(no_ex):
    global etats
    """ Reset de la liste etats"""
    etats=[]
    """ On ajoute chaque élément de l'exemple à la liste etats"""  
    for i in range (N):
       for j in range (N):
          etats.append (alphabet[no_ex][i][j])
    return(etats)
    
def test_cellule(cellule):
    global etats, poids, seuils
    """ On calcul la somme pondérée des entrées à laquelle on soustrait le seuil de la cellule"""
    c = -1
    somme = 0
    for i in range(N):
        for j in range(N):
            c += 1
            o = 0
            if etats[c]==True:
                o = 1
            somme = somme + o*poids[cellule][c]
    somme -= seuils[cellule]
    return(somme)
    
def delta(cellule) :
    global etats
    """ Calcul de l'erreur """
    x = 0
    d = test_cellule(cellule)
    y = etats[cellule]
    if etats[cellule] == True:
        x += etats.count(True)
    else : 
        x += etats.count(True)
        x += 1
    
    c_apprentissage = 0.314159265
    
    delta = (d - y + c_apprentissage) / x

    return(delta)
    
def modifie(cellule, erreur):
    global etats, poids, seuils
    
    for i in range (N_cell):
        if etats[i]:
           poids[cellule][i] = poids[cellule][i] + erreur
           poids[i][cellule] = poids[i][cellule] + erreur
    seuils[cellule] = seuils[cellule] - erreur

def apprend(exemple):
    global etats, seuils, poids
    
    sentinelle = True
    c = -1
    for i in range(N):
        for j in range(N):
            c += 1
            if test_cellule(c) > 0 and exemple[i][j] == False:
                modifie(c, - delta(c))
                sentinelle = False
                etats[c] = True
            elif test_cellule(c) <= 0 and exemple[i][j] == True:
                modifie(c, delta(c))
                sentinelle = False
                etats[c] = False
    print(sentinelle)
    return(sentinelle)

def test_forme(forme):
    global etats
    presente_exemple(forme)
    forme = etats.copy()
    c = True
    while c:
        c = False
        for i in range(N_cell):            
                if test_cellule(i) > 0 and forme[i] == False:
                    etats[i] = True
                    c = True
                    forme[i] = etats[c]
                elif test_cellule(i) <= 0 and forme[i] == True:
                    etats[i] = False
                    c = True
                    forme[i] = etats[i]
    print(etats)
    return(affiche_forme(etats))

    #---
initialise_reseau()
presente_exemple(0)
for j in range(10):
    for i in range(3):
        presente_exemple(i)
        apprend(alphabet[i])


    
