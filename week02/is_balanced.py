def is_number_balanced(number):

	
	if(number > 10):
		length = 0
		temp = number
		
		while temp > 0:
			temp //= 10
			length +=1
		
		sum = 0
		pow = 0

		while pow < length//2:
			sum += (number//(10**pow))%10
			pow+=1
		
		#print(sum)
		
		if length %2 != 0:
			pow+=1

		while pow <= length:
			sum -=(number//(10**pow))%10
			pow+=1
		
		#print(sum)
		
		if sum != 0:
			return False

	return True

#print((2324//10)%10)
number = int(input())
print(is_number_balanced(number))	