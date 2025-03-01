# find the incremental
def diff(k):
    other_points = k ** 2 - 1
    return (
        3 * (other_points - 2)
        + 4 * (other_points - 3)
        + 2 * (k - 4) * (other_points - 4)
        - (2 * k - 1) * (2 * k - 2) // 2
        + 2
    )


k = int(input())

print(0)
if k > 1:
    print(6)
if k > 2:
    result = 28
    print(result)
    for i in range(4, 1 + k):
        result += diff(i)
        print(result)
