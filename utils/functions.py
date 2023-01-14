def get_volume(volume) -> str:
	vol = volume.GetMasterVolumeLevelScalar() # Get it between 0 and 1
	vol = vol * 100 # To percentage
	vol = round(vol) # Round it
	return f"{vol}%" # Add the %

def show_elements(self, *elements):
	for element in elements:
		element.lift(self.frame)

def hide_elements(self, *elements):
	for element in elements:
		element.lower(self.frame)