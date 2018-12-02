x = input()
name = "PER"
count = 0
for i in range(len(x)):
    if x[i] != name[i%3]:
        count +=1
print(count)
