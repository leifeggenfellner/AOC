import math

with open("input.txt") as f:
    nums = [int(num) for num in f.readline().split(",")]
    mean = math.floor(sum(nums) / len(nums))
    print(sum(int((num - mean)*(num - mean + 1)/2) if num >
              mean else int((mean - num)*(mean - num + 1) / 2) for num in nums))
