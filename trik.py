x = input()
ball = 1
for i in (x):
  if i == "A" and ball % 3 == 1:
    ball += 1
  elif i == "A" and ball % 3 == 2:
    ball -= 1
  elif i == "B" and ball % 3 == 2:
    ball += 1
  elif i == "B" and ball % 3 == 0:
    ball -= 1
  elif i == "C" and ball %3 == 1:
    ball += 2
  elif i == "C" and ball %3 == 0:
    ball -= 2
    
print(ball)
