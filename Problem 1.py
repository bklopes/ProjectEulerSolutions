#Problem 1 - 'Multiples of 3 and 5'
#Find the sum of all the multiples of 3 or 5 below 1000.

total = 0
items = range(0, 1001)

for i in items:
	if i % 3 == 0 or i % 5 == 0:
		total += i

print total
