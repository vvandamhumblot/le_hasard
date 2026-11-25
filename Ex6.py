from random import randint

for i in range(100):
  r = randint(1, 10000)
  if r <= 1252:
    de = 1
  elif r <= 2642:
    de = 2
  elif r <= 4799:
    de = 3
  elif r <= 6786:
    de = 4
  elif r <= 7909:
    de = 5
  else:
    de = 6
  print(de)
