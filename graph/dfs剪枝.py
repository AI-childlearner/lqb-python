N=20
n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]

a=[0]+sorted(a,reverse=True)+[0]*(N-n-1)
sums = [0] * N
ans = 2e9

def dfs(u, res):
    global ans
    if res >= ans:
        return
    if u > n:
        ans = min(ans, res)
        return
    for i in range(1, res + 1):
        if sums[i] + a[u] <= m:
            sums[i] += a[u]
            dfs(u + 1, res)
            sums[i] -= a[u]
    sums[res + 1] = a[u]
    dfs(u + 1, res + 1)
    sums[res + 1] = 0
dfs(1, 1)
print(int(ans))
