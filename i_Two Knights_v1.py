k = int(input())

result = k ** 2 * (k ** 2 - 1) // 2

# find the amount if can attact


def cal(i, j, k):
    upper = j - 1
    lower = k - j
    left = i - 1
    right = k - i
    result = 0
    if upper >= 2 and left >= 1:
        result += 1
    if upper >= 2 and right >= 1:
        result += 1
    if lower >= 2 and left >= 1:
        result += 1
    if lower >= 2 and right >= 1:
        result += 1
    return result


for i in range(1, k + 1):
    for j in range(1, k + 1):
        result -= cal(i, j, k)

print(result)
