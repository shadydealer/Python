def group(set): 
	"""group(array) -> 2D array"""
	
	temp = []
	if len(set) > 0:

		subset_index = 0
		temp.append([set[0]])
		
		set_len = len(set)
		
		i = 1
		while i < set_len:
			if set[i-1] == set[i]:
				temp[subset_index].append(set[i])
			else:
				subset_index+=1
				temp.append([set[i]])
			i+=1
	return temp

def generate_keyboard(alphabet):
	s = 0
	amount = 3
	keyboard= []

	while s < len(alphabet) :
		if s == 15 or s == 22:
			amount = 4
		else:
			amount = 3
		keyboard.append([alphabet[s:s+amount]])
		s+=amount
	return keyboard

def generate_message(sequence, keyboard):
	
	result = ""
	presses = group(sequence)
	print(presses)
	is_upper_case = False
	
	char = ' '

	number = 0
	i = 0

	while i < len(presses):
		number = presses[i][0]
		
		if number == 1:
			is_upper_case = not is_upper_case
			continue
	
		if number == 0:
			string += ' '
			continue

		else:
			char = keyboard[number -2][len(presses[i])%len(keyboard[number-2])]
		
		if is_upper_case:
			char += char.capitalize()
			is_upper_case = False

		result += char
		i+=1
	print(result)


alphabet = "abcdefghijklmnopqrstuvwxyz"

keyboard = generate_keyboard(alphabet)
print(keyboard)
sequence = list(map(int, input().split()))

generate_message(sequence,keyboard)