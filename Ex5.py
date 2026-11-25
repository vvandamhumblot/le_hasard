from random import randint

for i in range(100):
  r = randint(1, 20)
  if r <= 2:
    de = 1
  elif r <= 5:
    de = 2
  elif r <= 8:
    de = 3
  elif r <= 11:
    de = 4
  elif r <= 14:
    de = 5
  else:
    de = 6
  print(de)
