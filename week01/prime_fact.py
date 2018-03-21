from math import sqrt

def prime_factorization(number):
	prime_facts = []
	

	#since 2 is the only even prime,
	#we can skill other even numbers
	#in the next iteration of we divide by 2 beforehand.
	if number > 1:
		
		counter = 0
		
		if (number % 2) == 0:
			while (number % 2) == 0:
				counter +=1
				number //=2
			prime_facts.append((2,counter))
	
		i = 3
		while i <= number:
			counter = 0
			while (number % i) == 0:
				counter +=1
				number //= i

			if counter > 0:
				prime_facts.append((i, counter))	
			i +=2
	print(prime_facts)

number = int(input("Enter integer to factorize: "))
prime_factorization(number)