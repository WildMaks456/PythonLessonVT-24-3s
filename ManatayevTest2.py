#Устанавливаем функцию
def remove_digits(s):
    primes ={'1','2','3','5','7','11','13','17','23'}#Делаем словарь простых чисел
    #возвращаем если функция пуста
    if s =="":
        return""
    #берем первый символ и делаем рекурсию
    first = s[0]
    if first in primes:
        return remove_digits(s[1:])
    else:
        return first + remove_digits(s[1:])
#Печатаем исход
print (remove_digits("abc123d4"))
