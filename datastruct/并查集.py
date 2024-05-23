n = 40010
p = [i for i in range(n)]
def get(x, y):
    return x * n + y

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

n, m = map(int, input().split())
for i in range(1, m + 1):
    x, y, ch = input().split()
    x, y = int(x) - 1, int(y) - 1
    a = get(x, y)
    if ch == 'R':
        b = get(x, y + 1)
    else:
        b = get(x + 1, y)
    pa, pb = find(a), find(b)
    if pa == pb:
        print(i)
        break
    p[pa] = pb
else:
    print("draw")
