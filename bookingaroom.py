import random
x = [int (i) for i in input().split()]
availRooms = []
takenRooms = []


for i in range(x[1]):
  takenRooms.append(int(input()))
for i in range(1, x[0]+1):
  if i not in takenRooms:
    availRooms.append(i)
if x[0] == x[1]:
  print("too late")
else:
  room = random.choice(availRooms)
  print(room)
