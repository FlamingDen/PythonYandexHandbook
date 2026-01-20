nums = list(map(int, input().split()))

ans = list()
for num in nums:
    curr_ans = {"digits": 0, "units": 0, "zeros": 0}
    while num != 0:
        curr = num % 2
        num //= 2
        if curr == 0:
            curr_ans["zeros"] += 1
        else:
            curr_ans["units"] += 1
        curr_ans["digits"] += 1
    ans.append(curr_ans)
print(ans)
