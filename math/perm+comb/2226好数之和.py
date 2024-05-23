l,r=map(int,input().split())
print(sum(set([x+10**i*2022+10**(i+4)*y for i in range(len(str(r))-4+1) for x in range(10**i) for y in range(l//(10**(i+4)),r//(10**(i+4))+1) if l<=x+10**i*2022+10**(i+4)*y<=r])))
import os
import sys

# 请在此输入您的代码

hao = set() #集合去重
# from itertools import combinations
ten = range(10)
for i in ten: #按位枚举所有1e9以内的好数
  for j in ten:
    for k in ten:
      for l in ten:
        for o in ten:
          hao.add(int(f"2022{i}{j}{k}{l}{o}"))
          hao.add(int(f"{i}2022{j}{k}{l}{o}"))
          hao.add(int(f"{i}{j}2022{k}{l}{o}"))
          hao.add(int(f"{i}{j}{k}2022{l}{o}"))
          hao.add(int(f"{i}{j}{k}{l}2022{o}"))
          hao.add(int(f"{i}{j}{k}{l}{o}2022"))

HAO = sorted(hao) #排序
ans = 0
for h in HAO:
  if l<=h<=r: #把满足要求的加起来
    ans+=h

print(ans)