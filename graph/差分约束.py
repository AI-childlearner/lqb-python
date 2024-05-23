from collections import deque

N = 100010
M = 300010

dist = [-float('inf')] * N
st = [False] * N
cnt = [0] * N
h = [-1] * N
idx = 0
e = [0] * M
ne = [0] * M
w = [0] * M

def add(a, b, c):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    w[idx] = c
    h[a] = idx
    idx += 1

def spfa():
    global idx
    dist[0] = 0
    q = deque([0])
    st[0] = True

    while q:
        u = q.pop()
        st[u] = False

        i = h[u]
        while i != -1:
            v = e[i]
            if dist[v] < dist[u] + w[i]:
                dist[v] = dist[u] + w[i]
                cnt[v] = cnt[u] + 1
                if cnt[v] > n:
                    return True
                if not st[v]:
                    q.append(v)
                    st[v] = True
            i = ne[i]
    return False

n, m = map(int, input().split())
for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 1:
        add(a, b, 0)
        add(b, a, 0)
    if x == 2:
        add(a, b, 1)
    if x == 3:
        add(b, a, 0)
    if x == 4:
        add(b, a, 1)
    if x == 5:
        add(a, b, 0)

for i in range(1, n + 1):
    add(0, i, 1)

if spfa():
    print("-1")
else:
    res = sum(dist[1:n + 1])
    print(res)
