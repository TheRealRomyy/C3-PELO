def get_volume(volume):
	vol = volume.GetMasterVolumeLevelScalar() # Get it between 0 and 1
	vol = vol * 100 # To percentage
	vol = round(vol) # Round it
	return f"{vol}%" # Add the %