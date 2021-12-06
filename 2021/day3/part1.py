with open("input.txt", "r") as f:
    arr = [0 for i in range(12)]
    data = f.readlines()
    for line in data:
        line = line.rstrip("\n")
        for i, bit in enumerate(line):
            if bit == "1":
                arr[i] += 1
    
    new_num = "0b"
    for num in arr:
        if num >= len(data) / 2:
            new_num += "1"
        else:
            new_num += "0"
    
    reversed_num = "0b" + "".join("1" if x == "0" else "0" for x in new_num[2:])
    
    print(int(new_num, 2) * int(reversed_num, 2))