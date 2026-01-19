porridges = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

n = int(input())

ln = len(porridges)
for i in range(n):
    print(porridges[i % ln])
