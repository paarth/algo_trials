def toStr(n,base):
	root_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if n < base:
		return root_string[n]
	else:
		return toStr(n//base,base) + root_string[n%base]

print(toStr(1453,16))	
