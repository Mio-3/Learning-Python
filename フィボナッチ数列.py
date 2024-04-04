def Fibonacci_func(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return Fibonacci_func(n-2) + Fibonacci_func(n-1)

n = int(input('整数nを入力してください'))
result = Fibonacci_func(n)
print(result) 