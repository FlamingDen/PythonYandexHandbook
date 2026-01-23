from itertools import product
from itertools import combinations

# Ваш стиль, но с циклическим поведением
suits = ["бубен", "пик", "треф", "червей"]
cards = ["10", "2", "3", "4", "5", "6", "7", "8", "9", "валет", "дама", "король", "туз"]
SUIT_MAP = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}

goal = SUIT_MAP.get(input(), "")
removed_card = input()
if removed_card in cards:
    cards.remove(removed_card)
prev = input()

all_suitable = []
for combo in combinations(product(cards, suits), 3):
    if any(suit == goal for _, suit in combo):
        string = ", ".join(f"{card} {suit}" for card, suit in combo)
        all_suitable.append(string)

print(all_suitable[all_suitable.index(prev) + 1])