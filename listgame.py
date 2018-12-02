k = int(input())
y = 0
i = 1
while (i * i <= k):
    if (k%i == 0):
        k = k/i
        y+=1
        i = 1
    if (k==1):
        y+=1
    i+=1
print(y)
