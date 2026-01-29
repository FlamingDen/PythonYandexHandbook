def can_eat(horse, other):
    x = abs(horse[0] - other[0])
    y = abs(horse[1] - other[1])
    
    if (x, y) == (2, 1) or (x, y) == (1, 2):
        return True
    return False