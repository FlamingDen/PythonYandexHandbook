def is_prime(num):
    if num == 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    
    for i in range(5, int(num**0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

print(is_prime(79701))