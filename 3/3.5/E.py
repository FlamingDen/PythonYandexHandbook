from sys import stdin


palindromes = set()
for line in stdin:
    words = line.rstrip("\n").split()
    for word in words:
        if word.lower() == word.lower()[::-1]:
            palindromes.add(word)
                        
print(*sorted(list(palindromes)), sep="\n")