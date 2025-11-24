#1
import math

x = float(input())
n = int(input())

def s(x, n, i, x_deg, fact, res):
	if i <= n:
		res += x_deg/math.sqrt(fact + i * i * i)   
		return s(x, n, i+1, x_deg*x, fact*(i+1), res)
	return res

print(s(x, n, 1, x_deg=x, fact=1, res=0))    

#2
n = input()

def sum_unique_digits(s, used = None, i=0):
	if used is None:
		used = set()
	if i == len(s):
     		return sum(int(x) for x in used)
	if s[i].isdigit():
		used.add(s[i])
	return sum_unique_digits(s, used, i+1)

print(sum_unique_digits(n))