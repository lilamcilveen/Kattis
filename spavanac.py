x = [int(i) for i in input().split()]

if(x[1] >= 45):
  print(x[0], x[1]-45)
elif(x[0] == 0):
  print(23, 60-(45-x[1]))
else:
  print(x[0]-1, 60-(45-x[1]))
