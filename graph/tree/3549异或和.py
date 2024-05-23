import sys

N = 100010
n, m, tot = 0, 0, 0
a = [0]*N
in_ = [0]*N
out = [0]*N
b = [0]*N
e = [[] for _ in range(N)]

def add(x, v):
    while x <= n:
        b[x] ^= v
        x += x & (-x)

def sum_(x):
    ans = 0
    if x == 0:
        return ans
    while x > 0:
        ans ^= b[x]
        x -= x & (-x)
    return ans

def rangeSum(l, r):
    return sum_(r) ^ sum_(l)

def dfs(u, fa):
    global tot
    in_[u] = tot = tot + 1
    for v in e[u]:
        if v == fa:
            continue
        dfs(v, u)
    out[u] = tot

def main():
    global n, m, tot
    n, m = map(int, sys.stdin.readline().split())
    a[1:n+1] = map(int, sys.stdin.readline().split())
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        e[u].append(v)
        e[v].append(u)
    dfs(1, 0)
    for i in range(1, n+1):
        add(in_[i], a[i])
    for _ in range(m):
        op, x, *extra = map(int, sys.stdin.readline().split())
        if op == 1:
            y = extra[0]
            v = rangeSum(in_[x] - 1, in_[x])
            add(in_[x], y ^ v)
        else:
            print(rangeSum(in_[x] - 1, out[x]))

if __name__ == "__main__":
    main()