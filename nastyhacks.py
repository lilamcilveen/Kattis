a = int(input())

for i in range (a):
  
  b = [int(x) for x in input().split()]
  
  r, e, c = b[0], 0, 0
  
  if(len(b) > 1):
    e = b[1]
  if(len(b) > 2):
    c = b[2]
  
  if ((e - c) > r):
    print("advertise")
    
  elif ((e - c) < r):
    print("do not advertise")
  
  else:
    print("does not matter")
