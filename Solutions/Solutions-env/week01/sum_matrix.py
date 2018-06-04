def sum_matrix(m):
	sum = 0
	for i in m:
		for j in i:
			sum += j
	print(sum)

m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
sum_matrix(m)