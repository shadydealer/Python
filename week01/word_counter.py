
word = input()
rows, cols = map(int, input().split())

def get_input():
	"""get_input() -> 2D array"""
	
	matrix = []
	for i in range(rows):
		matrix.append(input().split())

#	for subset in matrix:
#		print(subset)

	return matrix


move_x =[-1,0,1]
move_y =[-1,0,1]

def is_valid_index(x,y):
	"""is_valid_index(int, int) -> bool"""

	if x >= 0 and y >= 0  and x < cols and y < rows:
		return True
	return False

def count_occurance(matrix, x,y, str_ind):
	"""count_occurance(2D array, string) -> unsigned int"""

	for y in range(matrix):
		for x in range(matrix[i]): 	#matrix_char
			for k in range(word): 	#word_char
				if matrix[y][x] == word[k]:
					y+=move_y[j]
					x+=move_x[i]
				else:
					y-=move_y[j]*k
					x-=move_x[i]*k

matrix = get_input()	