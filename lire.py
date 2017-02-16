#coding : utf-8

#                                           ****Interragir avec les fichiers****

import datetime 

fich = "assnat.txt"

# Ouvrir le fichier
f = open(fich)

# Lire le fichier
# f.readlines()

lignes = f.readlines()

# voir ce que contient la variable «lignes»
for ligne in lignes : 
    #print(ligne.strip())
    # compléter les url (Aller voir la structure de l'URL sur le Web : http://www.assnat.qc.ca/fr/index.html)
    url = "http://www.assnat.qc.ca" + ligne.strip() 
    
    # Afficher juste les documents des débats de l'assemblée nationale
    # Qu'est-ce qu'il y a d'unique au url des débats de l'assemblée nationale ? Il y a une date !! On va aller chercher ça. 
    # (On ajoute une condition à la boucle pour afficher uniquement les urls qui ont une date)
    if "/201" in url:
        print(url)
        # TRAVAILLER AVEC DES DATES - extraire une date
        # 1) Au début du script, ajouter «import datetime», voir ligne 5
        date = url[90:98]
        print(date)
        d = datetime.datetime.strptime(date,"%Y%m%d")
        print(d.month)
