__points = 0


def move(player, number):
    global __points
    if player == "Петя":
        __points += number
    else:
        __points -= number


def game_over():
    return "Ничья" if __points == 0 else ("Петя" if __points > 0 else "Ваня")
