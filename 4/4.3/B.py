def recursive_digit_sum(num):
    if num == 0:
        return 0
    return num % 10 + recursive_digit_sum(num // 10)


result = recursive_digit_sum(7321346)
print(result)