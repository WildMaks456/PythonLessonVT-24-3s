def rec(n):
  if n != 0:
    expr = (2 * n + 1)
    return rec(n - 1) + 1 / (expr * expr)
  return 0

print(rec(1))
print(rec(2))
