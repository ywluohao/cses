n = int(input())
n_list = [int(x) for x in input().split()]
d = {i: i for i in n_list}

for i in range(1, n+1):
    if i not in d:
        print(i)
