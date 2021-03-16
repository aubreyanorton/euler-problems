#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def squareOfTheSum(numbers):
	return sum(numbers) ** 2

def sumOfTheSquares(squares):
	total = 0
	for square in squares:
		total = total + (square ** 2)
	return total 

rangeOfNumbers = range(1,101)
print(squareOfTheSum(rangeOfNumbers) - sumOfTheSquares(rangeOfNumbers) )

