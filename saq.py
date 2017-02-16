#coding : utf-8 

import csv

fichier = "saq.csv"
f1 = open(fichier)

#créer une variable ligne pour lire une ligne à la fois (fichier csv)
lignes = csv.reader(f1)
# pour commencer à la deuxième ligne (parce que l'on ne veut pas l'en-tête du fichier)
next(lignes)

toute = 0
france = 0
inventaire = 0

# Créer la boucle pour lire le fichier
for ligne in lignes : 
    #print(ligne)
# Afficher les pays seulement (5 le numéro de l'item)
    #print(ligne[5])
# Trouver le % des produits français :
    # 1) Créer un compteur total et france (lignes 11-12)
    toute += 1
    #if ligne[5] == "France" :
       #france += 1
#print(france/toute)

#Compter la valeur total de l'inventaire de la SAQ
# 1) Créer la variable « inventaire » ligne 15
    inventaire += float(ligne[15])
print(inventaire)

#POUR le devoir : besoin d'écrire un fichier et on ne l'a pas vu
# Nombre de page écrit de différentes façons
# Ajouter 3 colones : nombre de caractères dans le titre....
