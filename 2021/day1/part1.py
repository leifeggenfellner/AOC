with open("input.txt", "r") as f:
    nums = f.readlines()
    nums = [int(e) for e in nums]

    increased = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            increased += 1

    print(increased)
