# 4 вариант
def func(n):
	if n == 1:
		return 1
	return func(n-1)+((-1)*(-1*n))/((2*n+1)*n)

print(func(2))