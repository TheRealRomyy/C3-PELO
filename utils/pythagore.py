# Importer math
from math import *
from tkinter import *
from threading import Thread
import time

class Pythagore:

	GUI = None
	TIME = 0
	TYPE = 0

	def __init__(self, label, input_windows):
		self.time = 0
		self.ab = 0
		self.bc = 0

		self.label = label
		self.input_windows = input_windows

	def main(gui, res):
		Pythagore.GUI = gui
		if(Pythagore.TIME == 0):
			if(res != "1" and res != "2"):
				gui.label["text"] = "Erreur: Vous devez marquer 2 ou 1 !"
				gui.label["fg"] = "#FF0000"
				gui.hide_elements(gui, gui.send_button)
				gui.input_windows.delete(0, END)
				Thread(target=Pythagore.re_appear).start()
			elif res == "1":
				Pythagore.TIME += 1
				Pythagore.TYPE = 1
				Pythagore.hyphotenuse(Pythagore.TIME)
			else:
				Pythagore.TIME += 1
				Pythagore.TYPE = 2
				Pythagore.angle(Pythagore.TIME)
		else:
			Pythagore.TIME += 1
			if Pythagore.TYPE == 1:
				Pythagore.hyphotenuse(Pythagore.TIME)
			else:
				Pythagore.angle(Pythagore.TIME)

	def re_appear():
		time.sleep(3)
		Pythagore.GUI.show_elements(Pythagore.GUI, Pythagore.GUI.send_button)
		Pythagore.GUI.label["fg"] = "#000000"
		Pythagore.GUI.label["text"] = "Que voulez vous calculer ? \n \n1: L'hyphothènuse \n2: Un côté"

	def hyphotenuse(time):
		if(time == 1):
			Pythagore.GUI.input_windows.delete(0, END)
			Pythagore.GUI.label["text"] = "Veuillez donnez la longueur du premier côté ( AB )"
		elif(time == 2):
			Pythagore.ab = Pythagore.GUI.input_windows.get()
			Pythagore.GUI.input_windows.delete(0, END)
			Pythagore.GUI.label["text"] = "Veuillez donnez la longeur du deuxième côté ( BC )"
		elif(time == 3):
			Pythagore.bc = Pythagore.GUI.input_windows.get()
			Pythagore.GUI.input_windows.delete(0, END)
			Pythagore.GUI.label["text"] = "Bien, votre triangle ABC rectangle en B tel que AB = " + Pythagore.ab + " et BC = " + Pythagore.bc + " !"
		elif(time == 4):

			# Calculer l'hyphothènuse
			ac2 = float(Pythagore.bc)*float(Pythagore.bc) + float(Pythagore.ab)*float(Pythagore.ab)
			ac2 = sqrt(ac2)

			Pythagore.GUI.label["text"] = "L'hyphothènuse ( AC ) = " + str(ac2)
			Pythagore.GUI.hide_elements(Pythagore.GUI, Pythagore.GUI.send_button, Pythagore.GUI.input_windows)
			Pythagore.TIME = 0
			Pythagore.TYPE = 0

	# Creer la fonction angle
	def angle(time):
		if(time == 1):
			Pythagore.GUI.label["text"] = "Veuillez donnez la longueur du premier côté ( AB )"
			Pythagore.ab = Pythagore.GUI.input_windows.get()
			Pythagore.GUI.input_windows.delete(0, END)
		elif(time == 2):
			Pythagore.GUI.label["text"] = "Veuillez donnez la longeur du deuxième côté ( l'Hypothènuse )"
			Pythagore.hypo = Pythagore.GUI.input_windows.get()
			Pythagore.GUI.input_windows.delete(0, END)
		elif(time == 3):
			Pythagore.GUI.label["text"] = "Bien, votre triangle ABC rectangle en B tel que AB = " + Pythagore.ab + " et l'hyphothènuse = " + Pythagore.hypo + " !"
			Pythagore.GUI.input_windows.delete(0, END)

			# Calculer l'angle
			bc2 = float(Pythagore.hypo)*float(Pythagore.hypo) - float(Pythagore.ab)*float(Pythagore.ab)
			bc2 = sqrt(bc2)

			Pythagore.GUI.label["text"] = "L'angle ( BC ) = " + str(bc2)
			Pythagore.GUI.hide_elements(Pythagore.GUI, Pythagore.GUI.send_button, Pythagore.GUI.input_windows)
			Pythagore.TIME = 0
			Pythagore.TYPE = 0

