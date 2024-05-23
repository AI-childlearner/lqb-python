# 由于 Python 没有直接的数组索引从 1 开始的功能，因此需要稍微修改代码逻辑
# 但是，可以通过在数组前面添加一个虚拟元素来实现这个效果

T = int(input())
nlist,alist=[],[]
for _ in range(T):
    nlist+=[int(input())]
    alist+=[list(map(int, input().split()))]
for tt in range(T):
    n = nlist[tt]
    a=alist[tt]
    f = [[0, 0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        f[i][0] = max(f[i - 1][0], f[i - 1][1])
        f[i][1] = f[i - 1][0] + a[i - 1]
    print(max(f[n][0], f[n][1]))
for tt in range(T):
    n = nlist[tt]
    a=alist[tt]
    f = [[0, 0] for _ in range(2)]
    for i in range(1, n + 1):
        f[i & 1][0] = max(f[(i - 1) & 1][0], f[(i - 1) & 1][1])
        f[i & 1][1] = f[(i - 1) & 1][0] + a[i - 1]
    print(max(f[n & 1][0], f[n & 1][1]))
for tt in range(T):
    n=nlist[tt]
    a=[0]+alist[tt]
    f = [0] * (n + 1)  # 初始化 f 数组
    f[1] = a[1]
    for i in range(2, n + 1):
        f[i] = max(f[i - 1], f[i - 2] + a[i])
    print(f[n])

