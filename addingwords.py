defs = {}
while(True):
    try:
        x = input()
    except EOFError:
        break
    line = x.split(" ")
    if line[0] == "def":
        defs.update({line[1]: int(line[2])})
    elif line[0] == "clear":
        defs.clear()
    elif line[0] == "calc":
        calc = (line[1:len(line)-1])
        t = 0
        use = "+"
        for i in calc:
            if i == "+":
                use = "+"
            elif i == "-":
                use = "-"
            else:
                name = defs.get(i)
                if name == None:
                    t = "unknown"
                    break
                else:
                    if use == "+":
                        t += name
                    else:
                        t -= name
        t = next((k for k,v in defs.items() if v == t), "unknown")
        print(x[5:len(x)] + " " + str(t))
