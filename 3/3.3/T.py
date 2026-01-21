text = "ехали медведи на велосипеде"
print(
    {
        (first, second)
        for i, first in enumerate(sorted(text.lower().split()))
        for j, second in enumerate(sorted(text.lower().split()))
        if j > i and len(set(first) & set(second)) >= 3
    }
)
