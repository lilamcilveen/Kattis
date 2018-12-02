ops = [' + ', ' - ', ' * ', ' // ']

values = {}

for i in ops:
    for j in ops:
        for k in ops:
            result = "4{:s}4{:s}4{:s}4".format(i, j, k)
            index = eval(result)
            values[index] = result.replace('//', '/') + " = {:d}".format(index)

for i in range(0, int(input())):
    p = int(input())
    if  p > 256 or p < -60 or p not in values:
        print("no solution")
    else:
      print(values[p])
