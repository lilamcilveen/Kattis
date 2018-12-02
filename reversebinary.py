x = int(input())

bkwBinary = []
powers = []
decimalNumber = 0

while (x != 0):
  bkwBinary.append(x%2)
  x //= 2
  
for i in range (len(bkwBinary)-1, -1, -1):
  a = 2 ** i
  powers.append(a)

for i in range(len(bkwBinary)):
  decimalNumber += bkwBinary[i] * powers[i]
  
print (decimalNumber)
