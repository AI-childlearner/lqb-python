n=int(input())
import time
start=time.time()
import sys
sys.setrecursionlimit(500000)
dp=dict()
dp[(0,0)]=1
def dfs(i, j):
    if j==1:
        return 1
    if (i,j) in dp.keys():
        return dp[(i,j)]
    if i>j:
        dp[(i,j)] = dfs(i - j, j) + dfs(i - j, j - 1)
        return dp[(i,j)]
    else:
        return 0
print(dfs(n, 10))
print(time.time() - start)
import time
start=time.time()
dp=[[0]*11 for _ in range(n+1)]
#这里dp[i][j]代表将i拆分为j个互不相同的数的方案数

for i in range(1,n+1):#初始化很重要,需要严谨
    dp[i][1]=1 #将任意数拆分为1个的方案数为1
dp[0][0]=1 #将0划分为0个数的方案数为1

for i in range(1,n+1):
    for j in range(1,11):
        if i>j:
            #等式右边第一个表达式意思是：状态为最小值大于1，每个数都减去1
            #总和减去j个1，数量j不变的方案数。
            #第二个表达式的意思是：状态为最小值等于1，每个数都减去1，
            #总和减去j个1，数量少了一个最小值1，所以为j-1的方案数。
            #只能是这两个状态转化而来，所以相加，不存在在默认返回原始列表的0
            dp[i][j]=dp[i-j][j]+dp[i-j][j-1]
print(dp[n][10])
print(time.time()-start)