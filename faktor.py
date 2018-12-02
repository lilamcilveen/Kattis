x = [int(x) for x in input().split()]

a, i = x[0], x[1]

minS = (a * i) - a + 1

print(minS)
