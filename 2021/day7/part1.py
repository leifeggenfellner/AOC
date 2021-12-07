import statistics

with open("input.txt") as f:
    nums = [int(num) for num in f.readline().split(",")]
    median = int(statistics.median(nums))
    print(sum(num - median if num > median else median - num for num in nums))
