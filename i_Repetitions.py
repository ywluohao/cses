s = input()
max_count = 1
pointer1 = 0
pointer2 = 1
while pointer1 + pointer2 < len(s):
    if s[pointer1 + pointer2] == s[pointer1]:
        pointer2 += 1
    else:
        max_count = max(max_count, pointer2)
        pointer1 += pointer2
        pointer2 = 1

max_count = max(max_count, pointer2)
print(max_count)
