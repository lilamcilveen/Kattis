c = float(input())
l = int(input())
total = 0

for i in range (l):
  x = [float(i) for i in input().split()]
  total += c * (x[0]*x[1])
print(total)
