s = input()

num = s[0]
count = 0

for i in range(len(s)):
    if count == 0 or num == s[i]:
        count += 1
    
    if i == len(s) - 1:
        print(f"{num} {count}")
    elif num != s[i + 1]:
        print(f"{num} {count}")
        count = 0
        num = s[i + 1]
            
    