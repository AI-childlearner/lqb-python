n = int(input())
a = [int(input()) for _ in range(n)]

M = 1000010
cnt = [0] * M
ans = [0] * M

for num in a:
    cnt[num] += 1

for i in range(1, M):
    if cnt[i]:
        for j in range(i, M, i):
            ans[j] += cnt[i]

for num in a:
    print(ans[num] - 1)
