from itertools import product
from itertools import permutations
from itertools import cycle

suits = ["пик", "треф", "бубен", "червей"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]

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

res = sorted(list(product(cards, suits)))
ans = permutations(res, 3)

i = 1
for val in cycle(ans):
    if i > 10:
        break
    string = ", ".join(f"{n1} {n2}" for n1, n2 in val)
    if goal in string:
        print(string)
        i += 1
