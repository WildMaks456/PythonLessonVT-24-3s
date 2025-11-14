# 1
def rec(n):
    if n < 1:
        return 0
    return 1/((2*n+1)*(2*n+1)) + rec(n-1)
print("Задача 1")
print(rec(1))
print(rec(2))

# 2 Подсчитывает количество строк, состоящих только из заглавных букв, во вложенной хэш таблице print(count_uppercase({"a": "HELLO", "b": {"c": "world", "d": "OK"}}))
def count_uppercase(data):
    count = 0
    for value in data.values():
        if isinstance(value, str):
            if value.isalpha() and value.isupper():
                count += 1
        elif isinstance(value, dict):
            count += count_uppercase(value)
    return count

print("Задача 2")
print(count_uppercase({"a": "HELLO", "b": {"c": "world", "d": "OK"}}))
print(count_uppercase({"a": "HELLO", "b": {"c": "world", "d": "OK"}, "e": "AAAAA"}))



