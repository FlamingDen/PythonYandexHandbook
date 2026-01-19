letters = []
counts = []
while (s := input()) != "ФИНИШ":
    for letter in s:
        if letter == ' ':
            continue
        letter = letter.lower()
        if letter in letters:
            counts[letters.index(letter)] += 1
        else:
            letters.append(letter)
            counts.append(1)

ind_max = 0
max = 0
for i, val in enumerate(counts):
    if val > max:
        ind_max = i
        max = val
    elif val == max and letters[i] < letters[ind_max]:
        ind_max = i

print(letters[ind_max])
