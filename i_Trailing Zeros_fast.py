def f(n):
    result = 0
    while n >= 5:
        n //= 5
        result += n
    return result


print(f(int(input())))
