a = int(input())

def number_length(num):
    return len(str(num)) - (1 if num < 0 else 0) 

print(number_length(a))