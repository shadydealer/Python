def insertion_sort(birthdays):
	min_ind = 0
	temp = 0

	i = 0
	while i < len(birthdays) - 1:
		min_ind = i
		j = i + 1
		while j < len(birthdays):
			if birthdays[j] < birthdays[min_ind]:
				min_ind = j
			j+=1
		
		if min_ind != i:
			temp = birthdays[i]
			birthdays[i] = birthdays[min_ind]
			birthdays[min_ind] = temp
		
		i+=1

	return birthdays

def birthday_ranges(birthdays, ranges):

	result = []
	counter = 0
	for couple in ranges:
		for birthday in birthdays:
			if birthday > couple[1]:
				break
			if birthday >= couple[0]:
				counter +=1
		result.append(counter)
		counter = 0

	return result

#birthdays = [1,2,3,4,5]
#ranges = [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]

birthdays = [5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15]
ranges = [(4, 9), (6, 7), (200, 225), (300, 365)]
birthdays = insertion_sort(birthdays)

print(birthday_ranges(birthdays, ranges))