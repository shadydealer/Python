

def increasing_or_decreasing(seq):
	
	is_increasing = False
	is_decreasing = False

	if len(seq) > 1:

		if seq[0] < seq[1]:
			is_increasing = True
		elif seq[0] > seq[1]:
			is_decreasing = True

		if not is_increasing and not is_decreasing:
			return False

		i = 1
		if is_increasing:
			while i < len(seq) - 1:
				if seq[i] >= seq[i+1]:
					return False
				i+=1
			return "Up!"

		if is_decreasing:
			while i < len(seq) -1:
				if seq[i] <= seq[i+1]:
					return False
				i+=1
			return "Down!"		
	
	return False

seq = list(map(int, input().split()))
print(seq)

print(increasing_or_decreasing(seq))