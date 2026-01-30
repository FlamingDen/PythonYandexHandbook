def gcd(*nums: int) -> int:
    if len(nums) == 1:
        return nums[0]

    a = nums[0]
    for num in nums[1:]:
        b = num
        if a < b:
            a, b = b, a
        while b != 0:
            a %= b
            a, b = b, a
    return a