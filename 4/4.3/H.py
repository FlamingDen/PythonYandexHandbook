def fibonacci(n):
    result = []
    for i in range(n):
        if i <= 1:
            yield i
            result.append(i)
        else:
            curr = result[i - 1] + result[i - 2]
            yield curr
            result.append(curr)
    return result


print(*fibonacci(10))
