#coding: utf-8

# Construire un dictionnaire (en vert = la clé)
d = { 
    "nom": "Joly", 
    "prenom" : "Melanie",
    "circonscription" : "Ahunstic-Cartierville",
    "parti" : "Parti libéral du Canada",
    "coordonnées" : {
        "adresse" : "1450 rue Fleury, H2l 2m2",
        "courriel": "melanie.joly@hotmail.com"
    }
}
#Afficher les clés
#print(d.keys())

# Afficher les valeurs
#print(d.values())

# Afficher un élément précis
#print(d["circonscription"])

#Mettre une boucle dans un dictionnaire
#for x in d.values(): 
    #print(x)
    
for cle,valeur in d.items():
    print(cle,valeur)
