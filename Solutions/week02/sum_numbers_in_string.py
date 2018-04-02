def sum_of_numbers(string):
	
	number = "0"
	sum = 0

	for char in string:
		if char >= '0' and char <= '9':
			number+=char
		elif len(number) > 0:
			sum += int(number)
			number = "0"

	sum += int(number)
	return sum

string = input()
print(sum_of_numbers(string))