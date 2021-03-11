# What is the largest prime factor of the number 600851475143 ?

def largestPrimeFactor(number):
	largest = 0 # 0 means no prime numbers
	index = 2 # we're going to count upward from index until it's larger than the number or we have our prime number
	primes = [2]
	while index <= number:
		if not checkDivisible(index, primes):
			primes.append(index)
			if number % index == 0:
				largest = index
				while number % index == 0:
					number = number / index # we found a prime so we can divide them.
		index += 1
	return largest


# this checks to see if a number is divisible agaist a list of factors
def checkDivisible(number, listOfFactors):
	for factor in listOfFactors:
		if number % factor == 0:
			return True
	return False

print(largestPrimeFactor(600851475143))