s = input()

tmp = []
result = []

for l in s:
    if l in tmp:
        tmp.remove(l)
        result.append(l)
    else:
        tmp.append(l)

if len(tmp) > 1:
    print("NO SOLUTION")
elif len(tmp) == 1:
    print(''.join(result) + tmp[0] + ''.join(result[::-1]))
else:
    print(''.join(result) + ''.join(result[::-1]))
