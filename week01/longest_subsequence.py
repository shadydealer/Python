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


def max_consecutive(set):
	"""max_consecutive(array) -> integer"""
	temp = group(set)
	print(max(len(subset) for subset in temp))
		
#set = [1, 1, 1, 2, 3, 1, 1]
#set = [1, 2, 1, 2, 3, 3]
#set = [1,1,1,11,11,11,11,11,22,2,2,3,4,1,1,1,1,5,5,5,6]
#set = [1, 2, 3, 3, 3, 3, 4, 3, 3]
set = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]
#print(group(set))
max_consecutive(set)