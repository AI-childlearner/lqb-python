alldays=[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
n,m,k=map(int,input().split())
dp=[0]*366
for i in range(n):
  month,day,value=map(int,input().split())
  dp[alldays[month-1]+day]=max(dp[alldays[month-1]+day],value)#今年的第n天的票据值为当天票据的最大值
for i in range(1,366):
  dp[i]=max(dp[i-1],dp[i]+dp[max(0,i-k)] if dp[i]+dp[max(0,i-k)]<=m else -1)
print(dp[-1])