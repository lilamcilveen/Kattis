x = int(input())
total = 0
for i in range(x):
  a1 = input()
  power = int(a1) % 10
  a2 = a1[:-1]
  total += int(a2) ** power
print(total)
