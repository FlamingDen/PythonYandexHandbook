def find_mountains(heights):
    res = []
    for i in range(1, len(heights) - 1):
        curr = heights[i]
        if curr > heights[i - 1] and curr > heights[i + 1]:
            res.append(i + 1)
    return tuple(res)


result = find_mountains([5, 1, 10, 2, 3, 4, 3, 20])
print(result)