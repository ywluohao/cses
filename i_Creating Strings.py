from itertools import permutations

s = input()

temp = {"".join(t) for t in permutations(s)}
temp = sorted(temp)
print(len(temp))

for i in temp:
    print(i)
