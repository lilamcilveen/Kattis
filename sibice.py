x = [int(i) for i in input().split()]
for i in range (x[0]):
  m = int(input())
  dim = (x[1]**2 + x[2]**2)**(1/2)
  if (m <= dim):
    print("DA")
  else:
    print("NE")
