from itertools import combinations
s = input().split()

# k - length of subset
# n - length of set
k, n = int(s[0]), int(s[1])

a = list()
for x in range(n):
    a.append(x)
for z in combinations(a, k):
    s = ""
    for q in z:
        s += str(q)+ " "
    print(s)
