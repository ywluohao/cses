i = int(input())

if i in {2, 3}:
    print("NO SOLUTION")
elif i == 1:
    print(i)
else:
    left = list(range(5, i + 1, 2))
    right = list(range(6, i + 1, 2))
    result = left + [2, 4, 1, 3] + right
    print(*result)
