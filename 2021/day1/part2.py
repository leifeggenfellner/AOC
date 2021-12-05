with open("input.txt", "r") as f:
    data = f.readlines()
    data = [int(num) for num in data]

    sums = [data[i] + data[i+1] + data[i+2]
            for i in range(len(data)) if len(data) - (i+3) >= 0]
    print(sum(1 for i in range(1, len(sums)) if sums[i] > sums[i-1]))
