#импортируем модуль для факториалов
import math
#Устанавливаем функцию
def recursive_sum(x,n):
    #если число равно 1 возращаем с данной формулой
    if n ==1:
        return x**1 / (math.factorial(1)+1**2)
    #основное вычисление по формуле факториала
    return recursive_sum(x, n-1)+ x**n/(math.factorial(n)+n*n)
#Печатаем исход
print(recursive_sum(2,4))
