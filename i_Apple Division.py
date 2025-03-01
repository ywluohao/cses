a = input()
b = sorted(map(int, input().split()))

from itertools import combinations

total_sum = sum(b)
diff = total_sum

for i in range(len(b)):
    for t in combinations(b, i + 1):
        diff = min(diff, abs(2 * sum(t) - total_sum))

print(diff)
