import tkinter as tk
from utils.functions import *
from utils.pythagore import Pythagore

class GUI(tk.Tk):
	def __init__(self, volume):
		tk.Tk.__init__(self)
		self.volume = volume

		self.title("C3-PELO")
		self.geometry('500x500+50+50')

		self.frame = tk.Frame(self)
		self.frame.pack(fill="both", expand=True)

		GUI.buildGUI(self)

	def buildGUI(self):
		# Mute button
		mute_photo = tk.PhotoImage(file="res/mute.png").subsample(10,10)
		mute_btn = tk.Button(self, image=mute_photo, command= lambda: self.volume.SetMute(1, None))
		mute_btn.pack(in_=self.frame)

		# Unmute button
		unmute_photo = tk.PhotoImage(file="res/unmute.png").subsample(10,10)
		unmute_btn = tk.Button(self, image=unmute_photo, command= lambda: self.volume.SetMute(0, None))
		unmute_btn.pack(in_=self.frame)

		self.display_volume_label = tk.Label(text=get_volume(self.volume))
		self.display_volume_label.pack(in_=self.frame)

		# Update volume
		update_btn = tk.Button(text="update",command=self.update_with_volume)
		update_btn.pack(in_=self.frame)

		# Start pythagore button
		pythagore_photo = tk.PhotoImage(file="res/pythagore.png").subsample(10,10)
		pythagore_btn = tk.Button(self, image=pythagore_photo, command=lambda:self.pytha())
		pythagore_btn.pack(in_=self.frame)

		# Input windows
		self.input_windows = tk.Entry(self)
		self.input_windows.pack(in_=self.frame)
		GUI.hide_elements(self, self.input_windows)

		# Label
		self.label = tk.Label(self)
		self.label.pack(in_=self.frame)
		GUI.hide_elements(self, self.label)

		# Send button
		self.send_button = tk.Button(self, text="Envoie Zeubi", command=lambda: Pythagore.main(self, self.input_windows.get()))
		self.send_button.pack(in_=self.frame)
		GUI.hide_elements(self, self.send_button)

		self.mainloop()

	def pytha(self):
		self.label["text"] = "Que voulez vous calculer ? \n \n1: L'hyphothènuse \n2: Un côté"
		GUI.show_elements(self, self.input_windows, self.send_button, self.label)


	def update_with_volume(self):
		self.display_volume_label["text"] = get_volume(self.volume)

	def show_elements(self, *elements):
		for element in elements:
			element.lift(self.frame)

	def hide_elements(self, *elements):
		for element in elements:
			element.lower(self.frame)