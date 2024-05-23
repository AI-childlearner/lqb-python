from typing import List
import sys
sys.setrecursionlimit(200010)  # 将递归深度限制增加到 200010

n, m, num, t, sum, ans = 0, 0, 0, 0, 0, 0
N = 200010
c = [0] * N
siz = [0] * N
in_ = [0] * N
out = [0] * N
id_ = [0] * N
pos = [0] * N
cnt = [0] * N
tot = [0] * N
g = [[] for _ in range(N)]
q = [[0] * 2 for _ in range(N)]


def dfs(x: int):
    global num, t
    siz[x] = 1
    num += 1
    in_[x] = num
    id_[num] = x
    for y in g[x]:
        dfs(y)
        siz[x] += siz[y]
    out[x] = num
    t += 1
    q[t][0], q[t][1] = in_[x], out[x]


def add(x: int):
    global sum
    if cnt[c[x]] > 0:
        tot[cnt[c[x]]] -= 1
        if tot[cnt[c[x]]] == 0:
            sum -= 1
    cnt[c[x]] += 1
    tot[cnt[c[x]]] += 1
    if tot[cnt[c[x]]] == 1:
        sum += 1

def delete(x: int):
    global sum

    tot[cnt[c[x]]] -= 1
    if tot[cnt[c[x]]] == 0:
        sum -= 1
    cnt[c[x]] -= 1
    if cnt[c[x]] > 0:
        tot[cnt[c[x]]] += 1
        if tot[cnt[c[x]]] == 1:
            sum += 1


n = int(input())
m = int(n ** 0.5)
for i in range(1, n + 1):
    pos[i] = (i - 1) // m + 1
    c[i], fa = map(int, input().split())
    g[fa].append(i)
dfs(1)
q = q[1:n + 1]
q.sort(key=lambda x: (pos[x[0]], x[1] if (pos[x[0]] & 1) == 1 else -x[1]))
l, r = 1, 0
for ql, qr in q:
    while l > ql:
        l -= 1
        add(id_[l])
    while r < qr:
        r += 1
        add(id_[r])
    while l < ql:
        delete(id_[l])
        l += 1
    while r > qr:
        delete(id_[r])
        r -= 1
    if sum == 1:
        ans += 1
print(ans)