import math as m

x = float(input())


def f(x: float):
    return (
        m.log(m.pow(x, 3 / 16), 32)
        + m.pow(x, m.cos((x * m.pi) / (2 * m.e)))
        - (m.sin(x / m.pi)) ** 2
    )


print(f(x))
