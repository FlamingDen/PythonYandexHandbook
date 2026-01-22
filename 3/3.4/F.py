from itertools import product

suits = ["пик", "треф", "бубен", "червей"]
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "валет", "дама", "король", "туз"]

removed = input()
suits.remove(removed)
res = list(product(cards, suits))
print(*[f"{c} {s}" for c, s in res], sep="\n")

