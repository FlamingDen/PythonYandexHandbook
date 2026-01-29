count_of_pressing = 0


def click():
    global count_of_pressing
    count_of_pressing += 1


def get_count():
    return count_of_pressing
