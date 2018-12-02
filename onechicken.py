x = [int(i) for i in input().split()]
n, m = x[0], x[1]
p = abs(n-m)

if m > n and p == 1:
  print("Dr. Chaz will have", p, "piece of chicken left over!")
elif m < n and p == 1:
  print("Dr. Chaz needs", p, "more piece of chicken!")
elif m > n:
  print("Dr. Chaz will have", p, "pieces of chicken left over!")
else:
  print("Dr. Chaz needs", p, "more pieces of chicken!")
