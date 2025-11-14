#Variant 5
def count_uppercase(d):
  count = 0
  for val in d.values():
    if type(val) is dict:
      count += count_uppercase(val)
    elif val.isupper():
      count += 1
  return count

print(count_uppercase({"a": "HELLO", "b": {"c": "world", "d": "OK"}}))
print(count_uppercase({"a": "HELLO", "b": {"c": {"c1": "WOR", "c2": "ld"}, "d": "OK"}}))
print(count_uppercase({"a": "Hello", "b": {"c": "world", "d": "Ok"}}))