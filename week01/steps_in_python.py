import math

def sum_of_digits(n):
	n = abs(n)
	sum = 0	
	while n > 0 :
		sum += (n%10)
		n/=10
	print(sum)

def to_digits(n):
	arr = []
	while n > 0 :
		arr.append(n%10)
		n//=10
	arr.reverse()
	print(arr)
	
def to_number(digits):
	num =0
	for digit in digits:
		num *=10
		num += digit
	print (num)

def sum_of_factorials(n):
	n = abs(n)
	sum = 0	
	while n > 0 :
		sum += (math.factorial(n%10))
		n/=10
	print(sum)

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
	print(arr)

def fib_number(n):
	arr = []
	temp = 0
	i = 0
	if n >= 1:
		arr.append(1)
		while len(arr) <= n:
			print(arr[i], end = '')
			arr.append(arr[i] + temp)
			temp = arr[i]
			i+=1
	print()


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
	i = 0
	while i < len(string):
		j = 0
		while j < len(vowels):
			if string[i] == vowels[j]:
				counter +=1
				break
			j+=1
		i +=1
	print(counter)

def count_consonants(string):
	string = string.lower()
	vowels = "aeiouy"
	counter = 0
	i = 0
	while i < len(string):
		j = 0
		while j < len(vowels):
			if string[i] == vowels[j]:
				break
			j+=1
		if j == len(vowels):
			counter +=1
		i +=1
	print(counter)

def char_histogram(string):
	hist = {}
	for c in string:
		if not c in hist.keys():
			hist.update({c:1})
		else:
			hist[c] +=1
	print(hist)

num = int(input("Please enter a number: "))
sum_of_digits(num)
to_digits(num)
fibonacci(num)
sum_of_factorials(num);
fib_number(num)
to_number([1,2,3,0,2,3])

text = input()
print(palindrome(text))
count_vowels(text)
count_consonants(text)
char_histogram(text)