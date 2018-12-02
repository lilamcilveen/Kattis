a = [int(i) for i in input().split()]
x, y, n = a[0], a[1], a[2]

for i in range(1, n+1):
  if(i % x  == 0 and i % y == 0):
    print("Fizzbuzz")
  elif(i % x  == 0):
    print("Fizz")
  elif(i % y == 0):
    print("Buzz")
  else:
    print(i)
