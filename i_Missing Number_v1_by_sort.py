n = int(input())
n_list = [int(x) for x in input().split()]
n_sorted = sorted(n_list)
for i in range(n-1):
    if n_sorted[i] != i + 1:
        print(i + 1)
        break
else:
    print(n)
