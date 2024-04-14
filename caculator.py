def calculator_func(a,b,w):
  if w == '+':
    return a + b
  elif w == '-':
    return a - b
  elif w == '*':
    return a * b
  elif w == '/':
    if b != 0:
      return a / b
    else:
      return 'ゼロでの割り算はできません'
  else:
    return 'Error  計算不可能。'
  
#入力段階
a = int(input('整数を入力してください'))
b = int(input('整数を入力してください'))
w = input('演算子を入力してください (+, -, *, /): ')

num = calculator_func(a,b,w)
print(num)