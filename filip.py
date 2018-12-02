a = [int(i) for i in input().split()]
x, y = int(str(a[0])[::-1]), int(str(a[1])[::-1])

if(x > y):
  print (x)
else:
  print (y)
