nums = list(map(int, input().split()))

a = nums[0]
b = 0
for i in range(1, len(nums)):
    b = nums[i]
    if a < b:
        a, b = b, a
    while b != 0:
        a = a % b
        a, b = b, a
        
print(a)