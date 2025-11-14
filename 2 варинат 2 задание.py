def sum_digits(n)
    if n<10:
return n
  return n %10 sum_diligits(n // 10)