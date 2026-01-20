freq = dict()
while (s := input()) != "":
    row = list(s.split())
    for word in row:
        freq[word] = freq.get(word, 0) + 1

for key in freq:
    print(f"{key} {freq[key]}")