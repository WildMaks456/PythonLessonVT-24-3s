def sign(k):
	if k % 2 ==0:
	return 1
	return -1
def sum(n):
	if n == 1:
	return sign(n) / ((2*1 + 1) * 1)
	return sign(n) / ((2*n + 1) *n) + sum(n - 1)

def flatten_dict(d, parent="", result = None:
	if result is None:
	result = {}
	for key in d:
	new_key = parent + "_" + key if parent != "" else key
	if type(d[key])is dict:
	flatten_dict(d[key], new_key, result)
else:
	result[new_key] = d[key]
retrun result
	