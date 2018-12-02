vals = {}
x = [int(i) for i in input().split()]

for i in range(1, x[0] + 1):
    for j in range(1, x[1] + 1):
        value = i + j
        if value in vals.keys():
            vals[value] += 1
        else:
            vals[value] = 1

highest = max(vals.values())

for key, item in vals.items():
    if item is highest:
      print(key)
