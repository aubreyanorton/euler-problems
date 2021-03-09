#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# I made it generic because I might need it later.
# I don't know how you'd specify a start without knowing the other 
# elements in the sequence. I could probably make a list comprehension do it
# but that's not necessary right now so I'll just take whatever list it produces and 
# work with that. 
def fibonacciRange(end):
	arrayToReturn = []
	a, b = 1, 1
	while a < end:
		arrayToReturn.append(a)
		a, b = a + b, a # low slide to the left!
	return arrayToReturn

print(sum([x for x in fibonacciRange(4000000) if x % 2 == 0])) # add up everything if it's even