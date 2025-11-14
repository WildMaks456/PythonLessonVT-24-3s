sum = 0
counter = 0
factCounter = 0
factK = 1
factSum = 0
# вариант 3 
def factor(k):
	factK = 1+factK
	factSum = factSum + factK
	if (factCouner>=k):
		return factSum
	factor(k)



def recurs(n):
	fact = 1 
	if (counter>=n):
		return sum
	sum = sum + (1+(sin(counter)/factor(counter)))
	n=n+1
	recurs(n)

print(recurs(10))