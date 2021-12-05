with open("input.txt", "r") as f:
    nums = f.readlines()
    nums = [int(e) for e in nums]

    print(sum(1 for i in range(1, len(nums)) if nums[i] > nums[i-1]))
