import sys


def create_boards(arr):
    board = []
    boards = []

    for line in arr:
        if len(board) == 5:
            boards.append(board)
            board = []
        else:
            line = line.rstrip("\n").split(" ")
            nums = [int(num) for num in line if len(num)]
            board.append(nums)

    return boards


def check_for_bingo(board):
    total = 0
    bingo = False
    columns = [[] for i in range(len(board[0]))]

    for line in board:
        if not any(line):
            bingo = True
        for i, value in enumerate(line):
            columns[i].append(value)
            if isinstance(value, int):
                total += value
    for col in columns:
        if not any(col):
            bingo = True

    return total, bingo


with open("input.txt") as f:
    data = f.readlines()
    numbers = data[0].split(",")
    numbers = [int(num) for num in numbers]
    del data[:2]

    boards = create_boards(data)
    wins = []
    for number in numbers:
        for board in boards:
            for line in board:
                for i, num in enumerate(line):
                    if num == number:
                        line[i] = False

            total, bingo = check_for_bingo(board)
            if bingo:
                if board not in wins:
                    wins.append(board)
            if len(wins) == len(boards):
                print(
                    f"Sum: {total}", f"Last number: {number}")
                print(total * number)
                sys.exit()
