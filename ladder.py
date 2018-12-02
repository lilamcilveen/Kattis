import math
x = [int(i) for i in input().split()]

h, v = x[0], math.sin(math.radians(x[1]))


print(math.ceil(h / v))
