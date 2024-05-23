def dfs(u, last, num, sum):
    global ans, maxd
    if sum > maxd or (sum == maxd and num < ans):
        maxd = sum
        ans = num
    if u == 9:
        return
    for i in range(1, last + 1):
        if num * primes[u] > n:
            return
        num *= primes[u]
        dfs(u + 1, i, num, sum * (i + 1))

n = int(input())
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
ans = 0
maxd = 0
dfs(0, 30, 1, 1)
print(ans)
