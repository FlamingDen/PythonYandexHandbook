n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

power = int(input())
for num in nums:
    print(num**power)