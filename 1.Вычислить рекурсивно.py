Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def sum_rec(x, n):
...     # базовый случай
...     if n == 1:
...         return x / 1
...     def pow_rec(a, b):
...         if b == 1:
...             return a
...         return a * pow_rec(a, b - 1)
...     def fact_rec(k):
...         if k == 1:
...             return 1
...         return k * fact_rec(k - 1)
... 
...     return pow_rec(x, n) / fact_rec(n) + sum_rec(x, n - 1)
