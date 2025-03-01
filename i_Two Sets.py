n = int(input())

if n * (n+1) % 4:
    print('NO')
else:
    print('YES')
    sum = n * (n+1) // 4
    result = []
    i = n
    while sum > i:
        result.append(i)
        sum -= i
        i -= 1
    result.append(sum)
    print(len(result))
    print(*result)
    print(n - len(result))
    print(*(set(range(1, n + 1)) - set(result)))

# NOTE: good to know that we can use * to break down a list
