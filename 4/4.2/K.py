in_stock = {"coffee": 4, "milk": 4, "cream": 0}

MENU = {
    "Эспрессо": {"coffee": 1},
    "Капучино": {"coffee": 1, "milk": 3},
    "Макиато": {"coffee": 2, "milk": 1},
    "Кофе по-венски": {"coffee": 1, "cream": 2},
    "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "Кон Панна": {"coffee": 1, "cream": 1},
}


def can_cooked(drink: str) -> bool:
    need_for_cooked = MENU[drink]
    for ingredient in need_for_cooked:
        if in_stock[ingredient] < need_for_cooked[ingredient]:
            return False
    return True


def order(*preference) -> str:
    result = "К сожалению, не можем предложить Вам напиток"
    for drink in preference:
        if can_cooked(drink):
            result = drink
            need_for_cooked = MENU[drink]
            for ingredient in need_for_cooked:
                in_stock[ingredient] -= need_for_cooked[ingredient]
            break
    return result


print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
