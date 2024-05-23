n = int(input())
a = sorted([list(map(int, input().split())) for _ in range(n)],key=lambda x: x[0] + x[1])
m = sum([a[i][0] for i in range(n)])
f = [0] * (m + 1)
ans = 0
for i in range(n):
    for j in range(m, a[i][0] - 1, -1):
        if j - a[i][0] <= a[i][1]:f[j] = max(f[j], f[j - a[i][0]] + a[i][1])
        ans = max(ans, f[j])  # 更新最大价值
print(ans)