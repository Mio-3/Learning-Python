#年齢によって入場料を無料か、有料と表示する
age = int(input('整数を入力してください。'))

if age >= 0 and age <= 10: #0歳〜10歳までは無料
  print('入場料は無料です。')
elif age > 10 and age <= 65: #10歳から65歳までは入場料1500円
  print('入場料は1500円です。')
elif age > 65 and age <= 90: #65歳から90歳までは入場料750円
  print('入場料は750円です。')
else: #90歳以上も無料
  print('入場料は無料です。')