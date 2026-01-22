from itertools import product
from itertools import permutations
from itertools import cycle

suits = ["бубен", "пик", "треф", "червей"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
# cards = list(reversed(cards))

goal = ""
match input():
    case "буби":
        goal = "бубен"
    case "пики":
        goal = "пик"
    case "трефы":
        goal = "треф"
    case "черви":
        goal = "червей"

removed = input()
cards.remove(removed)
prev = input()

res = list(product(cards, suits))
ans = permutations(res, 3)

check = False
for val in cycle(ans):
    string = ", ".join(f"{n1} {n2}" for n1, n2 in val)
    if goal in string:
        if not check:
            if prev == string:
                check = True
        else:
            print(string)
            break
    print(string)
        



