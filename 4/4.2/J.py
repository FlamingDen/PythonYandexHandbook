def choice(*nums, **args):
    for key, val in args.items():
        curr_oper = min if "min" == key else max
    curr_func = val
    res = curr_func(nums[0])
    for num in nums[1:]:
        res = curr_oper(res, curr_func(num))
        
    return res

    