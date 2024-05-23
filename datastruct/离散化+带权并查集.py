mp = {}
p = list(range(10010))
d = [0] * 10010

def get(x):
    global mp
    if x not in mp:
        mp[x] = len(mp) + 1
    return mp[x]

def find(x):
    global p, d
    if p[x] != x:
        rx = find(p[x])
        d[x] += d[p[x]]
        p[x] = rx
    return p[x]

m = int(input())  # 我改为了input()，因为cin是用来读取输入的
n = int(input())
ans = m
for i in range(1, m + 1):
    x, y, s = input().split()
    x = get(int(x) - 1)
    y = get(int(y))
    t = 1 if s == "odd" else 0
    rx = find(x)
    ry = find(y)
    if rx == ry and abs(d[x] - d[y]) % 2 != t:
        ans = i - 1
        break
    elif rx != ry:
        p[ry] = rx
        d[ry] = abs(d[x] - d[y] - t)

print(ans)
