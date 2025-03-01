def how_many_5(n):
    result = 0
    while n % 5 == 0:
        result += 1
        n //= 5
    return result


print(sum(map(how_many_5, range(5, 1 + int(input()), 5))))
