
def palindrome(n):
	temp = str(n)
	i = 0
	while i <= len(temp)//2:
		if temp[i] != temp[-(i+1)]:
			return False
		i+=1
	return True


def get_largest_palindrome(number):

	if number == 0:
		return False

	number -=1
	#print(number)
	while palindrome(number) == False:
		number -=1

	return number

number = int(input())
print(get_largest_palindrome(number))