a = int(input())
b = int(input())

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a %= b
        a, b = b, a
    return a

print(gcd(a, b))