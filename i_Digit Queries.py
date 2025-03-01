l = [9]
for i in range(17):
    l.append(l[i] + (i + 2) * 9 * 10 ** (i + 1))

# i can also use a while loop to find the i,
# in that case, i do not need to hardcode 17


def c(n):
    if n <= 9:
        return n
    for i in range(17):
        if n <= l[i]:
            break

    q, r = divmod(n - l[i - 1] + i, i + 1)
    return int(str(10 ** (i) + q - 1)[r])


for _ in range(int(input())):
    print(c(int(input())))
