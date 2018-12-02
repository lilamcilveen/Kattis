counter = 0
b = int(input())
a = [int(x) for x in input().split()]
for i in range (b):
    if a[i] < 0:
      counter+=1
print(counter)
