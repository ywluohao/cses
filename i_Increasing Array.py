t = int(input())
lst = [int(i) for i in input().split()]

result = 0
for i in range(1, t):
    if lst[i - 1] > lst[i]:
        result += lst[i - 1] - lst[i]
        lst[i] = lst[i - 1]

print(result)
