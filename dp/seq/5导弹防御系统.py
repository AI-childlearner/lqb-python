N = 60
def dfs(u, up_cnt, down_cnt):
    global ans
    if up_cnt + down_cnt >= ans:#ans是最少的序列个数，剪枝
        return
    if u > n:
        ans = up_cnt + down_cnt#迭代到序列最后一个
        return
    #当前数放在上升序列中
    k = 1
    while k <= up_cnt and up[k] >= a[u]:#上升序列结尾大于等于序列当前值
        k += 1#记住可插值的上升序列的个数
    t = up[k]
    up[k] = a[u]
    if k <= up_cnt:#当前值大于上升序列值
        dfs(u + 1, up_cnt, down_cnt)#不单独开序列
    else:#迭代到序列末尾，作为单个新的上升序列
        dfs(u + 1, up_cnt + 1, down_cnt)#开上升序列
    up[k] = t#搜索结束，恢复状态
    #当前数放在下降序列中
    k = 1
    while k <= down_cnt and down[k] <= a[u]:
        k += 1
    t = down[k]
    down[k] = a[u]
    if k <= down_cnt:
        dfs(u + 1, up_cnt, down_cnt)
    else:
        dfs(u + 1, up_cnt, down_cnt + 1)
    down[k] = t
n = int(input())
up = [0] * N
down = [0] * N
a=[0]+list(map(int,input().split()))
ans = n
dfs(1, 0, 0)
print(ans)

