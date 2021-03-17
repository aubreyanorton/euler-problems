# what's the 10001st prime number?

# this checks to see if a number is divisible agaist a list of factors
def checkDivisible(number, listOfFactors):
	for factor in listOfFactors:
		if number % factor == 0:
			return True
	return False

def generatePrimes(number):
	index = 3 # we're going to count upward from index until it's larger than the number or we have our prime number
	primes = [2]
	while len(primes) < number:
		if not checkDivisible(index, primes):
			primes.append(index)
		index += 2 # we only count even numbers
	return primes

print(generatePrimes(10001)[-1:]) 

