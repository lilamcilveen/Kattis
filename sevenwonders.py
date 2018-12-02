x = input()
t, c, g = 0, 0, 0
for i in x:
  if i == "T":
    t += 1
  elif i == "C":
    c += 1
  else:
    g += 1
    
a = t ** 2 + c ** 2 + g ** 2
setCounter = 0

for i in range(len(x)):
  if(t > i and c > i and g > i):
    setCounter +=1
  else:
    break
  
total = (a + (7*setCounter))

print(total)
