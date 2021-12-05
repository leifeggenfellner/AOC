coords = []
max_num = 0

with open("input.txt") as f:
    for line in f.readlines():
        line = line.split(" ")
        del line[1]
        temp = []
        for coord_set in line:
            coords_temp = coord_set.split(",")
            coords_temp = [int(coord) for coord in coords_temp]
            temp.append(coords_temp)
            for coord in coords_temp:
                if coord > max_num:
                    max_num = coord
        coords.append(temp)

grid = [[0 for _ in range(max_num + 1)] for _ in range(max_num + 1)]

for coord_set in coords:
    if coord_set[0][0] != coord_set[1][0] and coord_set[0][1] != coord_set[1][1]:
        continue
    if coord_set[0][0] == coord_set[1][0]:
        iterables = [i for i in range(min(coord_set[0][1], coord_set[1][1]), max(
            coord_set[0][1], coord_set[1][1]) + 1)]
        for num in iterables:
            grid[num][coord_set[0][0]] += 1
    elif coord_set[0][1] == coord_set[1][1]:
        iterables = [i for i in range(min(coord_set[0][0], coord_set[1][0]), max(
            coord_set[0][0], coord_set[1][0]) + 1)]
        for num in iterables:
            grid[coord_set[0][1]][num] += 1


print(sum(1 for row in grid for num in row if num > 1))
