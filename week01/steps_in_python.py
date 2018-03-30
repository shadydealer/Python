import math

def sum_of_digits(n):
	n = abs(n)
	sum = 0	
	while n > 0 :
		sum += (n%10)
		n//=10
	return sum

def to_digits(n):
	arr = []
	if n == 0:
		arr.append(0)
	while n > 0 :
		arr.append(n%10)
		n//=10
	arr.reverse()
	return arr
	
def to_number(digits):
	num =0
	for digit in digits:
		num *=10
		num += digit
	return num

	
def fact_digits(n):
	sum = 0
	n = abs(n)
	if n == 0:
		sum = 1 
	while n > 0 :
		print(n)
		sum += (math.factorial((n%10)))
		n//=10
	return sum

def fibonacci(n):
	arr = []
	temp = 0
	i = 0
	if n >= 1:
		arr.append(1)
		while len(arr) < n:
			arr.append(arr[i] + temp)
			temp = arr[i]
			i+=1
	return arr

def fib_number(n):
	arr = fibonacci(n)
	result = ''
	for num in arr:
		result += str(num)
	return result

def palindrome(n):
	temp = str(n)
	i = 0
	while i <= len(temp)//2:
		if temp[i] != temp[-(i+1)]:
			return False
		i+=1
	return True


def count_vowels(string):
	string = string.lower()
	vowels = "aeiouy"
	counter = 0
	
	for char in string:
		if char in vowels:
			counter+=1
	
	return counter

def count_consonants(string):
	string = string.lower()
	consonants = "bcdfghjklmnpqrstvwxz"
	counter = 0

	for char in string:
		if char in consonants:
			counter+=1
	return counter

def char_histogram(string):
	hist = {}
	for c in string:
		if not c in hist.keys():
			hist.update({c:1})
		else:
			hist[c] +=1
	return hist

#num = 20
#sum_of_digits(num)
print(to_digits(123))
#fibonacci(num)
#print(fact_digits(111))
#print(fib_number(5))
#to_number([1,2,3,0,2,3])
#
#text = input()
#print(palindrome(text))
#count_vowels(text)
#count_consonants(text)
#char_histogram(text)