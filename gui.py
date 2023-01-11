import tkinter as tk
from utils.functions import *
from utils.pythagore import Pythagore

class GUI:
	def __init__(self, volume):
		self.volume = volume
		self.display_volume_label = None
		self.pythagore_result = None

	def buildGUI(self):
		root = tk.Tk()

		root.title("C3-PELO")
		root.geometry('500x500+50+50')

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

		input_windows = tk.Entry(root)
		input_windows.pack()

		label = tk.Label(root, text="Rien a dire")
		label.pack()

		pythagore = Pythagore(label, input_windows)

		pythagore_photo = tk.PhotoImage(file="res/pythagore.png").subsample(10,10)
		pythagore_btn = tk.Button(root, image=pythagore_photo, command=lambda: pythagore.first_display())
		pythagore_btn.pack()

		send_button = tk.Button(root, text="Entre trait", command=lambda: pythagore.result())
		send_button.pack()

		root.mainloop()

	def update_with_volume(self):
		self.display_volume_label["text"] = get_volume(self.volume)