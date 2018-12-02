x = [int(i) for i in input().split()]

if x[0] == 0 and x[1] == 0:
  print("Not a moose")
elif x[0] == x[1]:
  print("Even", x[0]+x[1])
elif x[0] > x[1]:
  print("Odd", x[0]*2)
else:
  print("Odd", x[1]*2)
