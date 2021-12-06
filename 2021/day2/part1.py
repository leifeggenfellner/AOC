with open("input.txt", "r") as f:
    data = f.readlines()
    data = [e.split(" ") for e in data]
    
    d = {}
    for e in data:
        try:
            d[e[0]] += int(e[1])
        except KeyError:
            d[e[0]] = int(e[1])
        
    print(d)
    
    horisontal = d["forward"]
    depth = d["down"] - d["up"]

    print(depth * horisontal)