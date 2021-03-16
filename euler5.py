#
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# they're asking us what the least common multiple of the range between [1-20] is
# so we have to factor all these numbers into their prime factors
# and find the set that contains all of them. Then we create the product of all of them.
# the problem statement is just another way of asking me what the least common multiple is.



def getPrimeFactors(number):
	if number <= 1:
		return None
	index = 2 # we're going to count upward from index until it's larger than the number or we have our prime number
	primes = {} # no primes are found yet
	while index <= number:
		if not checkDivisible(index, primes.keys()):
			if index not in primes:
				primes[index] = 0 # we found a new prime
			if number % index == 0:
				while number % index == 0:
					primes[index] += 1
					number = number / index # we found a prime so we can divide them.
		index += 1
	return primes


# this checks to see if a number is divisible agaist a list of factors
def checkDivisible(number, listOfFactors):
	for factor in listOfFactors:
		if number % factor == 0:
			return True
	return False

def leastCommonMultiple(numbers): # this takes an array of numbers
	primeFactorList = []
	lcmFactors = {}
	for number in numbers: 
		primeFactorList.append(getPrimeFactors(number))
	for primeFactor in primeFactorList:
		for entry in primeFactor.keys():
			if entry not in lcmFactors and (primeFactor[entry] > 0):
				lcmFactors[entry] = primeFactor[entry]
			elif entry in lcmFactors and lcmFactors[entry] < primeFactor[entry]:
				lcmFactors[entry] = primeFactor[entry]
	# we have our list of prime factors that come out of all our numbers. 
	# now we just go through them and find the product of all of them.
	product = 1
	for factor in lcmFactors.keys():
		for multiple in range(lcmFactors[factor]):
			product = product * factor 
	return product

print(leastCommonMultiple(range(2,21)))



