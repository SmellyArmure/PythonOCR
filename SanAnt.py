# 01 - Utiliser les comparateurs
# -*- coding: utf8 -*-
import random
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre.",
    "Il était une fois une princesse...",
    "C'est la mère Michel qui a perdu son chat",
    "Allons enfants de la patriiiie, le jour de gloire est arrivé",
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

def ChoixAuHasard(uneListe):
	return uneListe[random.randint(0, len(uneListe)-1)]

print("Bonjour à vous," + ChoixAuHasard(characters) + ".")

rep = "\n"
while rep!="B":
	rep=input("Taper entrée pour une nouvelle citation ou B pour quitter :  \n")
	if rep == "":
		print(ChoixAuHasard(quotes))
	else:
		"--> mauvaise réponse...on reboucle"
print("Merci, au-revoir")
"coucou"
input("--------FIN--------")