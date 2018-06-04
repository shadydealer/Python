def count_substring(haystack, needle):
	
	h_len = len(haystack)
	n_len = len(needle)

	beg = 0
	counter = 0

	while beg <= (h_len-n_len):
		if haystack[beg:(beg+n_len)] == needle:
			counter +=1
			beg += n_len
		else:
			beg+=1

	print(counter)

haystack = input("Please input string to check: ")
needle = input("Please input string to look for: ")

count_substring(haystack,needle)