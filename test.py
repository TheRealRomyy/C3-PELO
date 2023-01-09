def myinput(label : str, expected_type : type, opt : list = None) -> str:
	v = input(label)
	if(opt != None):
		if(expected_type == str):
			if(len(v) >= opt[0] and len(v) <= opt[1]):
				return v
			else:
				print("Error: Unexpected options")
		elif(expected_type == "int"):
			if(int(v) <= opt[0] and int(v) >= opt[1]):
				return v
			else: 
				print("Error: Unexpected options")
	return v

name = myinput("Comment t'appelles tu ?", int, [0, 9])
print("Bonjour " + name)