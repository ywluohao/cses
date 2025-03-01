# this is s math problem
# a = 2m + n
# b = m + 2n
# we want such (a,b) so that (m,n) are integers
# m = (2a-b)/3
# n = (2b-a)/3

for _ in range(int(input())):
    a, b = map(int, input().split())
    if (2 * a - b) % 3 == 0 and (2 * b - a) % 3 == 0 and (2 * a - b) >= 0 and (2 * b - a) >= 0:
        print("YES")
    else:
        print("NO")
