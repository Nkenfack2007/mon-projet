# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 12:43:53 2025

@author: NKENFACK
"""

#definition d'un dictionnaire 
d1 = {'pierre':17,'Paul':15, 'Jacques':16}
print (d1)
#ou
print(d1.items())
#nombre d'elements
print(len(d1))
#liste des cles
print(d1.keys())
#liste des valeur 
print(d1.values())
#acces a une valeur par cle 
print(d1['Paul'])
#ou
print(d1.get('Paul'))
#si cle n'existe pas 
#print(d1['Pipa'])


#modification 
d1['Jacques'] = 18
print(d1)
#ajouter un element 
d1['Henri'] = 22
print(d1)

#ajout d'un bloc d'elements
d1.update({'Monica':36, 'Bill':49})
print(d1)
