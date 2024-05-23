n=input()
l=list(map(int,input().split()))
a=set([0])
for i in l:
  for j in list(a):
    a.update(set([i+j,abs(i-j)])
print(len(a)-1) #排除掉重量为0