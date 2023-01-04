import tkinter as tk
from utils.functions import *

class GUI:
	def __init__(self, volume):
		self.volume = volume
		self.display_volume_label = None

	def buildGUI(self):
		root = tk.Tk()

		root.title("C3-PELO")
		root.geometry('300x200+50+50')

		mute_photo = tk.PhotoImage(file="res/mute.png").subsample(10,10)
		mute_btn = tk.Button(root, image=mute_photo, command= lambda: self.volume.SetMute(1, None))
		mute_btn.pack()

		unmute_photo = tk.PhotoImage(file="res/unmute.png").subsample(10,10)
		unmute_btn = tk.Button(root, image=unmute_photo, command= lambda: self.volume.SetMute(0, None))
		unmute_btn.pack()

		self.display_volume_label = tk.Label(text=get_volume(self.volume))
		self.display_volume_label.pack()

		update_btn = tk.Button(text="update",command=self.update_with_volume)
		update_btn.pack()

		pythagore_photo = tk.PhotoImage(file="res/pythagore.png").subsample(10,10)
		pythagore_btn = tk.Button(root, image=pythagore_photo)
		pythagore_btn.pack()

		root.mainloop()

	def update_with_volume(self):
		self.display_volume_label["text"] = get_volume(self.volume)