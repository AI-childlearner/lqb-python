def f():
    global a,n
    ans = 0
    for i in range(2, n + 1):
        if a[i - 1] + 1 != a[i]:
            ans += 1
    return (ans + 2) // 3

def dfs(depth, max_depth):
    global a,n
    if depth + f() > max_depth:
        return False
    if f() == 0:
        return True
    for length in range(1, n + 1):
        for l in range(1, n - length + 2):
            r = l + length - 1
            for k in range(r + 1, n + 1):
                w[depth] = a.copy()
                x, y = r + 1, l
                while x <= k:
                    a[y] = w[depth][x]
                    x += 1
                    y += 1
                x = l
                while x <= r:
                    a[y] = w[depth][x]
                    x += 1
                    y += 1
                if dfs(depth + 1, max_depth):
                    return True
                a = w[depth].copy()
    return False

T = int(input())
a = [0] * (20)
w = [[0]*(20) for _ in range(5)]
for _ in range(T):
    n = int(input())
    a[1:n+1] = list(map(int, input().split()))
    max_depth = 0
    while max_depth < 5 and not dfs(0, max_depth):
        max_depth += 1
    if max_depth == 5:
        print("5 or more")
    else:
        print(max_depth)
