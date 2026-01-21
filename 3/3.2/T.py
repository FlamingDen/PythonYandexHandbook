nums = list(set(map(int, input().split("; "))))
nums.sort()

res = {}
for i, num in enumerate(nums):
    # найти с какими оно взаимнопростое
    for j in range(i + 1, len(nums)):
        a = num
        b = nums[j]
        if a < b:
            a, b = b, a
        while b != 0:
            a = a % b
            a, b = b, a
        if a == 1:
            res[num] = res.get(num, []) + [nums[j]]
            res[nums[j]] = res.get(nums[j], []) + [num]
        
for key, val in sorted(res.items()):
    tmp = ", ".join(map(str, val))
    print(f"{key} - {tmp}")
