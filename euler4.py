
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

import math

def isPalindrome(number):
	numberArray = []
	numberCopy = number 
	while numberCopy != 0:
		numberArray.append(numberCopy % 10)
		numberCopy = numberCopy // 10
	reversedArray = list(numberArray) 
	numberArray.reverse()
	for i in range(0,len(reversedArray)):
		if numberArray[i] != reversedArray[i]:
			return False
	return True

largest = 0 

for i in range(100,999): # 
	for j in range(100,999):
		if isPalindrome(i * j) and largest < i * j:
			largest = i * j

print(largest)


