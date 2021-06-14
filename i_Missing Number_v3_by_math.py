n = int(input())
n_list = [int(x) for x in input().split()]

# we know the sum should be n*(n-1)/2
print(n*(n+1)//2 - sum(n_list))

# keep in mind of the problem of Interger Overflow

# improve it by:
total = 1
for i in range(2, n+1):
    total += i
    total -= n_list[i-2]

# second method: using XOR
# note:
# a1 ^ a2 ^ ... ^ a(n-1)  = a
# a1 ^ a2 ^ ... ^ a(n-1) ^ a(n)  = b
# then a ^ b = a(n)

x1 = n_list[0]
for i in n_list[1:]:
    x1 ^= i

x2 = 1
for i in range(2, n+1):
    x2 ^= i

print(x1 ^ x2)
