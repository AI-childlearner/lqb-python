N,K=map(int,input().split())
def C(a,b):
  ans=1
  for i in range(1,b+1):
    ans= ans*a//i
    a-=1
  return ans
import math
length=int(math.log(N,2))+1
cnt=C(length-1+(1 if int(math.log(N,2))==int(math.log(N+1,2))-1 else 0),K)
count=1
x=N
flag=length-2
while flag>=0 and K!=count-1:
  if x&(1<<flag):
    count+=1
    cnt+=C(flag,K-count+1)
  flag-=1
print(cnt)
#组合数函数
def C(a,b):
  ans=1
  for i in range(1,b+1):
    ans= ans*a//i
    a-=1
  return ans


x=bin(N)[2:]
le=len(x)
l=[]
for i in range(len(x)):
    if x[i]=='0':
        l.append(i)
co=0
count=0
#找出所有比当前数大的同位数二进制的个数
for i in l:
    t=i-co+1
    if K-t<0:
        break
    count+=C(le-1-i,K-t)
    co+=1
print(C(le,K)-count)