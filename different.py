while(True):
  try:
    x = [int(i) for i in input().split()]
  except EOFError:
    break
  x1, x2 = x[0], x[1]
  print(abs(int(x1)-int(x2)))
