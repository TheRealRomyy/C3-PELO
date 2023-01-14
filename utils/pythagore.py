# Importer math
from math import *
from threading import Thread
import tkinter as tk
from utils.functions import *
import time

class Pythagore:

	def __init__(self, root):
		self.time = 0
		self.type = 0

		self.ab = 0
		self.bc = 0

		self.label = root.label
		self.input_windows = root.input_windows
		self.send_button = root.send_button
		self.frame = root.frame
		self.pythagore_btn = root.pythagore_btn

	def main(self):
		self.label["text"] = "Que voulez vous calculer ? \n \n1: L'hyphothènuse \n2: Un côté"
		show_elements(self, self.input_windows, self.send_button, self.label)
		hide_elements(self, self.pythagore_btn)

	def response(self):
		res = self.input_windows.get() 
		if(self.time == 0):
			if(res != "1" and res != "2"):
				self.label["text"] = "Erreur: Vous devez marquer 2 ou 1 !"
				self.label["fg"] = "#FF0000"
				hide_elements(self, self.send_button, self.pythagore_btn)
				self.input_windows.delete(0, tk.END)
				Thread(target=self.re_appear).start()
			elif res == "1":
				self.time += 1
				self.type = 1
				self.hyphotenuse()
			else:
				self.time += 1
				self.type = 2
				self.angle()
		else:
			self.time += 1
			if self.type == 1:
				self.hyphotenuse()
			else:
				self.angle()

	def re_appear(self):
		time.sleep(3)
		show_elements(self, self.send_button, self.pythagore_btn)
		self.label["fg"] = "#000000"
		self.label["text"] = "Que voulez vous calculer ? \n \n1: L'hyphothènuse \n2: Un côté"

	def hyphotenuse(self):
		time = self.time
		if(time == 1):
			self.input_windows.delete(0, tk.END)
			self.label["text"] = "Veuillez donnez la longueur du premier côté ( AB )"
		elif(time == 2):
			self.ab = self.input_windows.get()
			self.input_windows.delete(0, tk.END)
			self.label["text"] = "Veuillez donnez la longeur du deuxième côté ( BC )"
		elif(time == 3):
			self.bc = self.input_windows.get()
			self.input_windows.delete(0, tk.END)
			self.label["text"] = "Bien, votre triangle ABC rectangle en B tel que AB = " + self.ab + " et BC = " + self.bc + " !"

			# Calculer l'hyphothènuse
			try:
				ac2 = float(self.bc)*float(self.bc) + float(self.ab)*float(self.ab)
				ac2 = sqrt(ac2)
			except ValueError:
				ac2 = "Valeur incorrectes !"

			self.label["text"] = "L'hyphothènuse ( AC ) = " + str(ac2)
			hide_elements(self, self.send_button, self.input_windows)
			show_elements(self, self.pythagore_btn)

	# Creer la fonction angle
	def angle(self):
		time = self.time
		if(time == 1):
			self.label["text"] = "Veuillez donnez la longueur du premier côté ( AB )"
			self.ab = self.input_windows.get()
			self.input_windows.delete(0, tk.END)
		elif(time == 2):
			self.label["text"] = "Veuillez donnez la longeur du deuxième côté ( l'Hypothènuse )"
			self.hypo = self.input_windows.get()
			self.input_windows.delete(0, tk.END)
		elif(time == 3):
			self.label["text"] = "Bien, votre triangle ABC rectangle en B tel que AB = " + self.ab + " et l'hyphothènuse = " + self.hypo + " !"
			self.input_windows.delete(0, tk.END)

			# Calculer l'angle
			try :
				bc2 = float(self.hypo)*float(self.hypo) - float(self.ab)*float(self.ab)
				bc2 = sqrt(bc2)
			except ValueError:
				bc2 = "Valeur incorrectes !"

			self.label["text"] = "L'angle ( BC ) = " + str(bc2)
			hide_elements(self, self.send_button, self.input_windows)
			show_elements(self, self.pythagore_btn)