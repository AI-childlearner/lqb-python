N,M,K=map(int,input().split())
W,V=[0]*(N+1),[0]*(N+1)#动态规划需要+1
for i in range(1,N+1):
  W[i],V[i]=map(int,input().split())
dp=[[[0,0] for _ in range(M+1)] for _ in range(N+1)]
for i in range(1,N+1):
  for w in range(W[i]):
    dp[i][w][0]=dp[i-1][w][0]#不操作也要算进去
    dp[i][w][1]=dp[i-1][w][1]#不操作也要算进去
  for w in range(W[i],M+1):
    dp[i][w][0]=max(dp[i-1][w-W[i]][0]+V[i],dp[i-1][w][0])
    dp[i][w][1]=max(dp[i-1][w-W[i]][1]+V[i],dp[i-1][w][1])
    if w>=K+W[i]:
      dp[i][w][1]=max(dp[i][w][1],dp[i-1][w-K-W[i]][0]+2*V[i])
print(max(dp[N][M][0],dp[N][M][1]))#不需要遍历求最大值