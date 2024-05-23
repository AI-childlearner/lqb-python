from collections import deque
import copy
n1=input()
n2=input()
n=n1+n2
def ind(i):
  if i==0:return [1,3]
  if i==1:return [0,2,4]
  if i==2:return [1,5]
  if i==3:return [0,4]
  if i==4:return [1,3,5]
  if i==5:return [2,4]
c=set()
c.add(n)
q=deque([])
for i in range(len(n)):
  if n[i]==' ':
    q.append((n,i,0))
  if n[i]=='A':
    p1=i
  if n[i]=='B':
    p2=i
while q:
  k,x,z=q.popleft()
  if k[p1]=='B' and k[p2]=='A':
    print(z)
    break
  for i in ind(x):
    a=i
    t=list(copy.copy(k))
    t[a],t[x]=t[x],t[a]
    t=''.join(t)
    if t not in c:
      c.add(t)
      q.append((t,a,z+1))