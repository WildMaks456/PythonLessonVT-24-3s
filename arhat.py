def S(n, x):
    if n==1:
        return x**1 /(1**3+1)
    return S(n-1, x) + x **(n*n)/(n**3+n)

n = 5 
x = 2
result = S(n, x)
print (result)