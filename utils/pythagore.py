# Importer math
from math import *

class Pythagore:

	def __init__(self, label, input_windows):
		self.time = 0
		self.ab = 0
		self.bc = 0

		self.label = label
		self.input_windows = input_windows

	def first_display(self):
		self.label["text"] = "Que voulez vous calculer ? \n \n1: L'hyphothènuse \n2: Un côté"
	def result(self):
		self.time = self.time + 1
		self.input_windows.delete(0, "end")

		if(self.time == 1):
			res = self.input_windows.get()
			if res != "1" and res != "2":
				self.label["text"] = "Erreur: Vous deviez marqué 2 ou 1 !"
				exit()

			if res == "1":
				self.hyphothenuse(self.time)
			# elif res == "2":
			# 	self.angle(label)
		
	def hyphotenuse(self, time):
		if(time == 2):
			self.label["text"] = "Veuillez donnez la longueur du premier côté ( AB )"
			self.ab = self.input_windows.get()
		elif(time == 3):
			self.label["text"] = "Veuillez donnez la longeur du deuxième côté ( BC )"
			self.bc = self.input_windows.get()
		else:
			self.label["text"] = "Bien, votre triangle ABC rectangle en B tel que AB = " + self.ab + " et BC = " + self.bc + " !"

			# Calculer l'hyphothènuse
			ac2 = float(self.bc)*float(self.bc) + float(self.ab)*float(self.ab)
			ac2 = sqrt(ac2)

			self.label["text"] = "L'hyphothènuse ( AC ) = " + str(ac2)

	# Creer la fonction angle
	def angle(label):
		label["text"] = "Veuillez donnez la longueur du premier côté ( AB )"
		ab = input()

		label["text"] = "Veuillez donnez la longeur du deuxième côté ( l'Hyphothènuse )"
		hypo = input()

		label["text"] = "Bien, votre triangle ABC rectangle en B tel que AB = " + ab + " et l'hyphothènuse = " + hypo + " !"

		# Calculer l'angle
		bc2 = float(hypo)*float(hypo) - float(ab)*float(ab)
		bc2 = sqrt(bc2)

		label["text"] = ("BC = " + str(bc2))