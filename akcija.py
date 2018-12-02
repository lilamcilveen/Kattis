c = []
n = int(input())
total = 0
     
for i in range (n):
  c.append(int(input()))
  
totalC = sum(c)
discount = sum(sorted(c, reverse=True)[2::3])

print(totalC - discount)
