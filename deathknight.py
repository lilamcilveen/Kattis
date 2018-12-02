n = int(input())
w = 0
for i in range(n):
  k = input()
  if "CD" not in k:
    w += 1
print(w)
