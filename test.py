def myinput(label : str, expected_type : type, opt) -> str:
	v = input(label)
	if(type(v) != expected_type):
	    print("Error: Unexpected input type")
    if(opt != None):
        if(expected_type == str):
            if(len(v) >= opt[0] and len(v) <= opt[1]):
                v
            else:
                print("Error: Unexpected options")
	    elif(expected_type == "int"):
            if(v <= opt[0] and v >= opt[1]):
                v
            else: 
                print("Error: Unexpected options")

myinput("Comment t'appelles tu ?", str)