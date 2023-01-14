from tkinter import *
from utils.functions import *
from utils.pythagore import Pythagore

class GUI(Tk):
	def __init__(self, volume):
		Tk.__init__(self)
		self.volume = volume

		self.frame = Frame(self)
		self.label = Label(self)
		self.input_windows = Entry(self)
		self.send_button = Button(self, text="Envoie Zeubi", command=lambda: self.pytha.response())

		self.pytha = None

		self.buildGUI()

	def buildGUI(self):
		self.title("C3-PELO")
		self.geometry('500x500+50+50')

		# Frame
		self.frame.pack(fill="both", expand=True)

		# Mute button
		mute_photo = PhotoImage(file="res/mute.png").subsample(10,10)
		mute_btn = Button(self, image=mute_photo, command= lambda: self.volume.SetMute(1, None))
		mute_btn.pack(in_=self.frame)

		# Unmute button
		unmute_photo = PhotoImage(file="res/unmute.png").subsample(10,10)
		unmute_btn = Button(self, image=unmute_photo, command= lambda: self.volume.SetMute(0, None))
		unmute_btn.pack(in_=self.frame)

		display_volume_label = Label(text=get_volume(self.volume))
		display_volume_label.pack(in_=self.frame)

		# Update volume
		update_btn = Button(text="update",command=lambda:self.update_with_volume(display_volume_label))
		update_btn.pack(in_=self.frame)

		# Input windows
		self.input_windows.pack(in_=self.frame)
		hide_elements(self, self.input_windows)

		# Label
		self.label.pack(in_=self.frame)
		hide_elements(self, self.label)

		# Send button
		self.send_button.pack(in_=self.frame)
		hide_elements(self, self.send_button)

		# Start pythagore button
		pythagore_photo = PhotoImage(file="res/pythagore.png").subsample(10,10)
		self.pythagore_btn = Button(self, image=pythagore_photo, command=lambda:self.pytha_btn())
		self.pythagore_btn.pack(in_=self.frame)

		# Exit button
		exit_button = Button(text="Exit", fg="#FF0000", command=lambda:exit())
		exit_button.pack()

		self.mainloop()

	def update_with_volume(self, label : Label):
		label["text"] = get_volume(self.volume)
	
	def pytha_btn(self):
		self.pytha = Pythagore(self)
		self.pytha.main()