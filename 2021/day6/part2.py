with open("input.txt") as f:
    fishes = [int(num) for num in f.readline().split(",")]
    fish = [fishes.count(i) for i in range(9)]
    for _ in range(256):
        num = fish[0]
        fish = fish[1:]
        fish[6] += num
        fish.append(num)
    print(sum(fish))

# Alternative option with dictionary
# with open("input.txt") as f:
#     fishes = [int(num) for num in f.readline().split(",")]
#     fish = {i: fishes.count(i) for i in range(9)}
#     for _ in range(256):
#         num = fish[0]
#         fish[0], fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7], fish[8] = fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7] + num, fish[8], num
#     print(sum(value for value in fish.values()))