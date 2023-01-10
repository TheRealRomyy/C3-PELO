# Importer math
from math import *

class Pythagore:
	def main_pythagore(label, result):
		# Demander ce qu'on veut calculer
		label["text"] = "Que voulez vous calculer ? \n \n1: L'hyphothènuse \n2: Un côté"
		toCalc = result
		
		# Vérifier si toCalc n'est ni 2 ni 1
		if toCalc != "1" and toCalc != "2":
			label["text"] = "Erreur: Vous deviez marqué 2 ou 1 !"
			exit()

		# Si toCalc est 1 calculer l'hyphothènuse si c'est 2 calculer un angle
		if toCalc == "1":
			hyphothenuse(label)
			
		elif toCalc == "2":
			angle(label)


	# Creer la fonction hyphothènuse
	def hyphothenuse(label):
		label["text"] = "Veuillez donnez la longueure du premier côté ( AB )"
		ab = input()

		label["text"] = "Veuillez donnez la longeure du deuxième côté ( BC )"
		bc = input()

		label["text"] = "Bien, votre triangle ABC rectangle en B tel que AB = " + ab + " et BC = " + bc + " !"

		# Calculer l'hyphothènuse
		ac2 = float(bc)*float(bc) + float(ab)*float(ab)
		ac2 = sqrt(ac2)

		label["text"] = "L'hyphothènuse ( AC ) = " + str(ac2)

	# Creer la fonction angle
	def angle(label):
		label["text"] = "Veuillez donnez la longueure du premier côté ( AB )"
		ab = input()

		label["text"] = "Veuillez donnez la longeure du deuxième côté ( l'Hyphothènuse )"
		hypo = input()

		label["text"] = "Bien, votre triangle ABC rectangle en B tel que AB = " + ab + " et l'hyphothènuse = " + hypo + " !"

		# Calculer l'angle
		bc2 = float(hypo)*float(hypo) - float(ab)*float(ab)
		bc2 = sqrt(bc2)

		label["text"] = ("BC = " + str(bc2))