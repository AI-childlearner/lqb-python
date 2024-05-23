import os
import sys

# 请在此输入您的代码
isprime=[1]*2023
isprime[0]=0
isprime[1]=0
l=[]
for i in range(2,2023):
  if isprime[i]:
    for j in range(2,2022//i+1):
      isprime[i*j]=0
    l.append(i)
dp=[[0]*2023 for i in range(1+len(l))]
for i in range(1,1+len(l)):
  for j in range(2023):
    if j<l[i-1]:
      dp[i][j]=dp[i-1][j]
      continue
    dp[i][j]=max(dp[i-1][j],dp[i-1][j-l[i-1]]+1)
print(max([dp[i][2022] for i in range(1+len(l))]))