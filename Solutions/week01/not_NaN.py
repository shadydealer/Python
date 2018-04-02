def nan_expand(times):
	if times >= 1:
		output = ""
		while times > 0:
			output += "Not a "
			times -=1
		output += "NaN"
		print(output)

times = int(input("times to expand: "))
nan_expand(times)