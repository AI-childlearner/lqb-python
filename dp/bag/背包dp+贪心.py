test_case = 1
N = 110
M = 100010

class Node:
    def __init__(self, s, e, l):
        self.s = s
        self.e = e
        self.l = l

T = int(input())
for _ in range(T):
    f = [-float('inf')] * M
    f[0] = m = 0
    n = int(input())
    a = [None] * (n + 1)
    for i in range(1, n + 1):
        s, e, l = map(int, input().split())
        a[i] = Node(s, e, l)
        m += a[i].s
    def mycmp(x,y):
        return x.s*y.l-x.l*y.s
    import functools
    a=a[:1]+sorted(a[1:],key = functools.cmp_to_key(mycmp))
    for i in range(1, n + 1):
        for j in range(m, a[i].s - 1, -1):
            f[j] = max(f[j], f[j - a[i].s] + a[i].e - (j - a[i].s) * a[i].l)
    ans = max(f)
    print(f"Case #{test_case}: {ans}")
    test_case += 1
