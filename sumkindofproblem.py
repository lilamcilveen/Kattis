p = int(input())
for i in range(p):
  s = [int(x) for x in input().split()]
  k, n = s[0], s[1]
  s1 = int(n*(n+1)/2)
  s2 = n**2
  s3 = n*(n+1)
  print(k, s1, s2, s3)
