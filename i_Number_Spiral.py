def c(y, x):
    if (y >= x and y % 2 == 1) or (y < x and x % 2 == 1):
        x, y = y, x
    if y >= x:
        return y ** 2 - x + 1
    else:
        return (x - 1) ** 2 + y


for _ in range(int(input())):
    y, x = map(int, input().split())
    print(c(y, x))
