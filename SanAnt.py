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
    12,
    "calimero",
    ["bonjour", "bonsoir"],
    "casper", 
    "le chat potté", 
    3,
    "Kirikou",
]

def ChoixAuHasard(uneListe):
	return uneListe[random.randint(0, len(uneListe)-1)]

def MetUneCapitale(uneListe):
	i=0
	for element in uneListe:
		if isinstance(element, str):
			uneListe[i]=uneListe[i].capitalize()
			#element=element.capitalize() : ne marche pas !!!
		else:
			uneListe[i]="chaîne n°"+str(i)
			print("ATTENTION l'élément n°" + str(i) + " N'ETAIT PAS UNE CHAINE mais un" + str(type(element)))
		i+=1
	return uneListe


print("Bonjour à vous," + ChoixAuHasard(MetUneCapitale(characters)) + ".")

rep = "\n"
while rep!="B":
	rep=input("Taper entrée pour une nouvelle citation ou B pour quitter : ")
	if rep == "":
		print("C'est {personnage} qui a dit : {citation}".format(personnage=ChoixAuHasard(characters),citation=ChoixAuHasard(quotes)))
		#print("C'est {} qui a dit : {}".format(ChoixAuHasard(characters),ChoixAuHasard(quotes))) # en plus condensé
	else:
		"--> mauvaise réponse...on reboucle"
print("Merci, au-revoir")
"coucou"
input("--------FIN--------")