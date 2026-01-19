s = input().lower()

lf = 0
r = len(s) - 1

palindrome = "YES"
while lf < r:
    while s[lf] == " ":
        lf += 1
    while s[r] == " ":
        r -= 1
    if lf >= r:
        break
    if s[lf] != s[r]:
        palindrome = "NO"
        break
    lf += 1
    r -= 1

print(palindrome)
