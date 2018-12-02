t = int(input())
for i in range(t):
    skipBlank = input()
    n = int(input())
    sum = 0
    for j in range(n):
        sum+= int(input())
    if (sum % n == 0):
        print("YES")
    else:
      print("NO")
