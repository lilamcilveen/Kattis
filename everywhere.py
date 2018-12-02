x = int(input())
for i in range(x):
    cities = {}
    f = int(input())
    for j in range(0, f):
        cities[input()] = 1
    print(len(cities))
