
# NOTE: good to know that we can use Counter or we can create the Counter by ourself.
# s = input()
# [(i, s.count(i)) for i in set(s)]

from collections import Counter

c = Counter(input())
left = ''
tmp = 0
mid = ''
for (v, i) in c.items():
    if i % 2 == 0:
        left += (i // 2) * v
    elif i % 2 == 1:
        tmp += 1
        mid = i * v
    if tmp > 1:
        print("NO SOLUTION")
        break
if tmp <= 1:
    print(left + mid + left[::-1])


# refactoring:
#     print(left + (mid if mid else "") + left[::-1])
# =>  print(left + (mid or "") + left[::-1])
