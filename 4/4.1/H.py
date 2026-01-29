def fragments(numbers):
    res = []
    curr_list = []
    for num in numbers:
        if not curr_list or curr_list[-1] < num:
            curr_list.append(num)
        else:
            res.append(curr_list)
            curr_list = [num] 
    if curr_list:
        res.append(curr_list)
    return res    
        
            
result = fragments([6, 2])     
print(result)         
        