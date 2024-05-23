mp = {}
idx = 0
N = 200010
p = [i for i in range(N)]

def s(x):
    global idx, mp
    if x in mp:
        return mp[x]
    mp[x] = idx
    idx += 1
    return idx - 1

def find(x):
    global p
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

T = int(input())
for _ in range(T):
    idx = 1
    mp = {}
    m = int(input())
    for i in range(1, N):
        p[i] = i
    r = []
    for _ in range(m):
        a, b, e = map(int, input().split())
        a = s(a)
        b = s(b)
        r.append((a, b, e))
        if e:
            p[find(a)] = find(b)
    success = True
    for i in range(m):
        if not r[i][2]:
            a, b = r[i][0], r[i][1]
            if find(a) == find(b):
                success = False
                break
    if success:
        print("YES")
    else:
        print("NO")
