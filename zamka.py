l, d, x = int(input()), int(input()), int(input())

n, m = 0, 0

for i in range(l, d+1):
  if sum([int(x) for x in str(i)]) == x:
    n = i
    break
  
for i in range(d, l-1, -1):
  if sum([int(x) for x in str(i)]) == x:
    m = i
    break
  
print(n)
print(m)
