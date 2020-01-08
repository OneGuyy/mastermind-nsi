#Wikiwand du Mastermind (EN) : https://www.wikiwand.com/en/Mastermind_(board_game)
import random


#Cette fonction permet de remplir de manière aléatoire le Master
def nouveauMaster(listeCouleur): #Done
	couleurMaster = []
	for i in range(4):
		indexAleatoire = random.randint(0, 6)
		couleurMaster.append(listeCouleur[indexAleatoire])
	return couleurMaster

#Cette fonction permet de 
def nouveauJoueur(listeCouleur): #Done
	couleurJoueur = []
	while len(couleurJoueur) < 4:
		couleurDonnee = input("Choisissez une lettre parmi celles possibles : ").upper()
		if couleurDonnee in listeCouleur:
			couleurJoueur.append(couleurDonnee) 
		else:
			print("Erreur ! La lettre ne fais pas partie de la liste !")
	return couleurJoueur

def bienPlaces(master, joueur):
	jetonsBienPlaces = 0
	for i in range(4):
		if jeuMaster[i] == joueur[i]:
			jetonsBienPlaces += 1
	return jetonsBienPlaces



def malPlaces(master, joueur):
	copieMaster = master.copy()
	mauvaisePlace = []

	for i in range(4):
		if copieMaster[i] == joueur[i]:
			copieMaster[i] = 0
			joueur[i] = 1

	for i in range(4):
		if joueur[i] in copieMaster:
			mauvaisePlace.append(joueur[i])
			copieMaster[copieMaster.index(joueur[i])] = 0
			joueur[i] = 1

	return len(mauvaisePlace)


#Listes des couleurs / lettres possibles (7 lettres)
ensembleCouleurs = ["A", "B", "C", "D", "E", "F", "G", "0"]
print("Lettres Possibles : " + str(ensembleCouleurs[:6]), end="\n\n")

#Compteur de tours
compteur = 0

#Au tour du Master

jeuMaster = ['A', 'A', 'E', 'B']

while True:
	compteur += 1
	print("Tour " + str(compteur) + " :\n")

	#Au tour du joueur
	jeuJoueur = nouveauJoueur(ensembleCouleurs)
	print(jeuJoueur)

	print()

	#On compte les pions bien placés
	PionsBiensPlaces = bienPlaces(jeuMaster, jeuJoueur)
	print("Pions à la bonne place : " + str(PionsBiensPlaces)) 


	#On compte les pions mal placés
	PionsMalPlaces = malPlaces(jeuMaster, jeuJoueur)
	print("Pions à la mauvaise place : " + str(PionsMalPlaces))

	print()

	if PionsBiensPlaces == 4:
		print("Victoire en " + str(compteur) + " tours !")
		break