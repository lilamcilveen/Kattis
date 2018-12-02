c = {}
x, y = 0, 0
for i in range (3):
  c[i] = [int(i) for i in input().split()]
if c[0][0] == c[1][0]:
  x = c[2][0]
elif c[1][0] == c[2][0]:
  x = c[0][0]
else:
  x = c[1][0]
  
if c[0][1] == c[1][1]:
  y = c[2][1]
elif c[1][1] == c[2][1]:
  y = c[0][1]
else:
  y = c[1][1]
print(x, y)
