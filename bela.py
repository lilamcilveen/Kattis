x = input().split()
n, b = int(x[0]) *4, x[1]
p = 0
for i in range(n):
  c = input()
  #dominant and affected by it
  if c[1] == b and c[0] == "J": 
    p += 20
  elif c[1] == b and c[0] == "9":
    p += 14
  #not dominant and affected
  elif c[0] == "J": 
    p += 2
  #doesn't matter
  elif c[0] == "A":
    p += 11
  elif c[0] == "K":
    p += 4
  elif c[0] == "Q":
    p += 3
  elif c[0] == "T":
    p += 10
  else:
    p += 0
print(p)
