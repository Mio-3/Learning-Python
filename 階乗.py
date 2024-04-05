#サンプルコード
def factorial(n):
  if n == 0: # 0の階乗は0なので、n=0の時、返り値は0となる。
    return 0
  elif n == 1:  # 1の階乗の値は、どうやっても1なので、n=1の時、返り値は1となる。
    return 1
  else:
    return n * factorial(n-1) 
  # 階乗は1〜nまでの値をどんどん掛け算していくので、再帰関数を用いると例えばn=3の時は 3*2*1より return 3 * (factorial(2) = 2 * factorial(1)) * 1となる。

n = int(input('整数nを入力してください')) # 整数nの値を入力してもらう
result  = factorial(n) # result変数に、factorial関数の値を代入する
print(result) # result変数を出力
