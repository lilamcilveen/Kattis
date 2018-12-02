x = int(input())
n = int(input())
saveUp = x

for i in range (n):
  p = int(input())
  saveUp += (x - p)

print(saveUp)
