def find_value(data, most_or_least_common):
    data_copy = data.copy()
    i = 0
    
    while len(data_copy) > 1:
        bit1 = []
        bit0 = []
        
        for line in data_copy:
            if line[i] == "1":
                bit1.append(line)
            else:
                bit0.append(line)
        
        if most_or_least_common == "most":
            if len(bit1) >= len(bit0):
                for num in bit0:
                    data_copy.remove(num)
            else:
                for num in bit1:
                    data_copy.remove(num)
        elif most_or_least_common == "least":
            if len(bit1) < len(bit0):
                for num in bit0:
                    data_copy.remove(num)
            else:
                for num in bit1:
                    data_copy.remove(num)
    
        i += 1
    
    return data_copy[0]

with open("input.txt", "r") as f:
    data = f.readlines()
    data = [e.rstrip("\n") for e in data]

    oxygen = "0b" + find_value(data, "most")
    co2 = "0b" + find_value(data, "least")

    print(int(oxygen, 2) * int(co2, 2))

