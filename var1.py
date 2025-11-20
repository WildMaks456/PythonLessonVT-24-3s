#1 
x = float(input())
n = int(input())

def s(x, n):
    if n == 1:
        return x
    def p(a, b):
        return 1 if b == 0 else a * p(a, b-1)
    def f(k):
        return 1 if k <= 1 else k * f(k-1)
    return p(x, n) / (f(n) + n * n)

print(s(x, n))

#2 
s = ("abc123d4")

def remove_digits(s):
    if s == '':
	return ''
    return ('' s[0].isdigit() else s[0]) + remove_digits(s[1:])

print (remove_digits(s))

    
    
