x = int(input())
while(x != (-1)):
  d = 0
  Matrix = {}
  time = {}
  newTime = {}
  
  for i in range(x):
    Matrix[i] =[int(j) for j in input().split()]
  
  for i in range(x):
    time[i] = Matrix[i][1]
  
  newTime[0] = time[0]
  for i in range (0, x-1):
    newTime[i+1] = abs(time[i] - time[i+1])
  
  for i in range(x):
    d += (Matrix[i][0] * newTime[i])
    
  print(d, " miles")
  x = int(input())
